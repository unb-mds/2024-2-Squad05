#!/bin/bash
# Collect static files
# echo "Collect static files"
# python src/manage.py collectstatic --noinput
# Apply database migrations
echo "Apply database migrations" 
python src/manage.py migrate 
# Start server
echo "Starting server" 
python src/manage.py runserver 0.0.0.0:8000
# python 