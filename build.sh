#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
python wanbang/manage.py collectstatic --no-input
python wanbang/manage.py migrate
