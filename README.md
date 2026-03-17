# devops-interview

## Setup

To start up the development environment, you will run `make provision`.

## Assignment
Using the provided Docker image, write a Helm chart that deploys both the FastAPI server and Celery
worker. The chart should launch:

- An API workload that runs the container with the `api` entrypoint (equivalent to `docker run <image> api`).
- A worker workload that runs the container with the `celery` entrypoint (`docker run <image> celery`).

Your Helm definitions should set any required environment variables (Redis/Postgres details, queue
names, etc.) and expose the FastAPI service appropriately.
