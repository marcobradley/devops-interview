# devops-interview

## Recommended: Use GitHub Codespaces

**This assignment is designed to be completed in [GitHub Codespaces](https://github.com/features/codespaces).** You should open this repo in a Codespace rather than running it locally. Codespaces provides a pre-configured cloud environment with Docker and all required tooling available out of the box, so you can get started immediately without any local setup.

To open in Codespaces: fork this repository or create a branch, then click the green **Code** button, select the **Codespaces** tab, and click **Create codespace**. Working in a fork or branch lets you commit and push your changes freely. Note that the initial Codespace creation may take up to 10 minutes, so be patient while it sets up.

## Setup

Once inside your Codespace (or local environment), start up the development environment by running `make provision`.

## Assignment
Using the provided Docker image, write a Helm chart that deploys both the FastAPI server and Celery
worker. The chart should launch:

- An API workload that runs the container with the `api` entrypoint (equivalent to `docker run ghcr.io/tagup/devops-interview:latest api`).
- A worker workload that runs the container with the `celery` entrypoint (`docker run ghcr.io/tagup/devops-interview:latest celery`).

Your Helm definitions should set any required environment variables (Redis/Postgres details, queue
names, etc.) and expose the FastAPI service appropriately.
