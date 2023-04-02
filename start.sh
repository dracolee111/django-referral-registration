#!/usr/bin/env bash

set -o errexit  # exit on error

#python manage.py background_process & # define your background process, eg. a scheduler

gunicorn core.wsgi --log-file=-
