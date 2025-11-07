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

Write-Host "Starting Django development server..."
cd webtravel
python manage.py runserver