# Script to setup and run the webtravel Django project

# Check if the virtual environment directory exists
if (-not (Test-Path -Path ".venv")) {
    Write-Host "Creating virtual environment..."
    python -m venv .venv
}

# Activate the virtual environment, install requirements, and run the server
Write-Host "Activating virtual environment and installing requirements..."
.\.venv\Scripts\Activate.ps1

pip install -r webtravel\requirements.txt

Write-Host "Creating default superuser (root:root) if it doesn't exist..."
cd webtravel
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='root').exists() or User.objects.create_superuser('root', 'root@example.com', 'root')"

Write-Host "Starting Django development server..."
python manage.py runserver