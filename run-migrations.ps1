# Running makemigrations
Write-Host "Running makemigrations"
docker exec lumina-web python src/manage.py makemigrations

# Apply database migrations
Write-Host "Apply database migrations"
docker exec lumina-web python src/manage.py migrate

# Create superuser
Write-Host "Create superuser"
docker exec lumina-web python src/manage.py createsuperuser