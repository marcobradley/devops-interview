#!/bin/bash
set -euo pipefail

if [ $# -eq 0 ]; then
  set -- api
fi

command="$1"
shift || true

case "$command" in
  api)
    exec /app/entrypoints/api.sh "$@"
    ;;
  celery)
    exec /app/entrypoints/celery.sh "$@"
    ;;
  *)
    exec "$command" "$@"
    ;;
esac
