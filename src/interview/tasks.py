import os
from datetime import datetime, timezone

import redis
from sqlalchemy import create_engine, text

from interview.worker import celery_app

redis_client = redis.Redis.from_url(os.environ["REDIS_URI"], decode_responses=True)
engine = create_engine(os.environ["DATABASE_URI"])


@celery_app.task
def increment():
    redis_client.incrby("page_views", 1)


@celery_app.task
def aggregate_page_views():
    lock = redis_client.lock("lock:page_views", timeout=30, blocking_timeout=5)

    if not lock.acquire(blocking=True):
        raise RuntimeError("Could not acquire Redis lock")

    try:
        count = int(redis_client.get("page_views") or 0)
        if count == 0:
            return

        with engine.begin() as connection:
            connection.execute(
                text(
                    """
                    INSERT INTO page_views (time, count)
                    VALUES (:time, :count)
                    """
                ),
                {
                    "time": datetime.now(timezone.utc),
                    "count": count,
                },
            )

        redis_client.delete("page_views")
    finally:
        lock.release()