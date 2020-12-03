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

exec gunicorn -t 120 -b 0.0.0.0:5000 --workers 3 --access-logfile - --error-logfile - --forwarded-allow-ips="192.168.1.19" flask_app:app
