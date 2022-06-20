#!/bin/bash

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Run database migrations
echo "Run database migrations"
python manage.py migrate

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000