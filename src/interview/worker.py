from celery import Celery
from kombu import Exchange, Queue


def create_celery_app() -> Celery:
    modules = ["interview.tasks"]

    app = Celery(
        "interview",
        include=modules,
    )

    default_exchange = Exchange("default", type="direct", durable=True)

    default_queue = Queue(
        "default",
        exchange=default_exchange,
        routing_key="default",
        durable=True,
    )

    app.conf.update(
        task_default_queue="default",
        task_default_exchange="default",
        task_default_routing_key="default",
        task_queues=[default_queue],
        task_track_started=True,
        task_acks_late=True,
        task_reject_on_worker_lost=True,
        worker_prefetch_multiplier=1,
        result_expires=3600,
        worker_hijack_root_logger=False,
        worker_redirect_stdouts=False,
        worker_log_color=False,
    )

    return app


celery_app: Celery = create_celery_app()
