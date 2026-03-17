#!/bin/bash
set -euo pipefail

exec uvicorn interview.api:app --host 0.0.0.0 --port 5000 --workers 2 "$@"
