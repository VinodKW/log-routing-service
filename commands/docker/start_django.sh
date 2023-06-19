#!/bin/sh

# Wait for MySQL to start
while ! bash -c 'echo > /dev/tcp/mysql/3306' >/dev/null 2>&1; do
  echo 'Waiting for MySQL to start...'
  sleep 1
done

# Execute the Django commands
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
