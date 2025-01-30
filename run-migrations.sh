#!/bin/bash
# Collect static files
# echo "Collect static files"
# docker exec lumina-web python src/manage.py collectstatic --noinput
# Running makemigrations
echo "Running makemigrations" 
docker exec lumina-web python src/manage.py makemigrations 
# Apply database migrations
echo "Apply database migrations" 
docker exec lumina-web python src/manage.py migrate 