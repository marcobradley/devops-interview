import os
from fastapi import FastAPI

from interview.tasks import increment, aggregate_page_views

app = FastAPI(root_path="/api/v1")

aggregate_queue = os.environ.get("AGGREGATE_QUEUE", "default")
increment_queue = os.environ.get("INCREMENT_QUEUE", "default")

@app.post("/increment")
async def increment_api() -> str:
    increment.apply_async(queue=increment_queue)
    return "ok"

@app.post("/aggregate")
async def aggregate_api() -> str:
    aggregate_page_views.apply_async(queue=aggregate_queue)
    return "ok"