#!/bin/sh
source venv/bin/activate

while true; do
    flask deploy
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo Deploy command failed, retrying in 5 secs...
    sleep 5
done

exec gunicorn -t 120 -b :5000 --workers 3 --access-logfile - --error-logfile - flask_app:app