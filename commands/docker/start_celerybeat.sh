#!/bin/bash

# Wait for MySQL to start
while ! bash -c 'echo > /dev/tcp/mysql/3306' >/dev/null 2>&1; do
  echo 'Waiting for MySQL to start...'
  sleep 1
done

# Wait for Django server to start
while ! bash -c 'echo > /dev/tcp/django-server/8000' >/dev/null 2>&1; do
  echo 'Waiting for django-server to start...'
  sleep 1
done

# Start the specified container
celery -A logservice beat --loglevel=info