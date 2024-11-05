#!/bin/bash

# Wait for postgres
while ! nc -z db 5432; do
  echo "Waiting for postgres..."
  sleep 1
done

cd src

python manage.py migrate
python manage.py collectstatic --no-input

exec "$@" 