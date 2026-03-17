#!/bin/bash
set -euo pipefail

exec celery -A interview.worker worker --concurrency 1 --queues default "$@"
