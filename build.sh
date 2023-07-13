#!/usr/bin/env bash
set -o errexit

pip instakk -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate