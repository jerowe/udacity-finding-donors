#!/usr/bin/env bash

set -x -e

## There is no earthly reason why redis should take 5 minutes, but here we are
echo "Waiting for redis"

#chmod 777 /home/flask/finding_donors_flask_app/wait-for-it.sh
bash /home/flask/finding_donors_flask/wait-for-it.sh --host redis --port 6379 --timeout 300

echo "Complete waiting for redis"

gunicorn --workers=4 --bind=0.0.0.0:5000 --keep-alive=2000 --timeout=2000 --log-level=debug flask_app:app
