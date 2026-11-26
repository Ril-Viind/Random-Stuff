#!/bin/bash
# Developer helper: start/stop the Pathly backend locally.
cd "$(dirname "$0")"
set -e

VENV=".venv/bin/uvicorn"
LOG="/tmp/opencode/uvicorn.log"

case "${1:-start}" in
  start)
    pkill -f "uvicorn app.main" 2>/dev/null || true
    sleep 1
    DATABASE_URL="sqlite:///./pathly.db" \
    AUTO_CREATE_TABLES=true \
    setsid nohup $VENV app.main:app --host 127.0.0.1 --port 8000 > "$LOG" 2>&1 < /dev/null &
    disown || true
    sleep 4
    echo "Backend started. Log: $LOG"
    ;;
  stop)
    pkill -f "uvicorn app.main" 2>/dev/null || true
    echo "Backend stopped."
    ;;
  *)
    echo "Usage: $0 [start|stop]"
    exit 1
    ;;
esac