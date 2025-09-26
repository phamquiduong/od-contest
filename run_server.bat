@echo off
REM ==============================================
REM Django Setup Script
REM ==============================================

REM Upgrade pip
python -m pip install --upgrade pip

REM Install requirements
pip install -r requirements.txt

REM Set up environment variables for Django
if not exist ".env" (
    echo Copying .env.example to .env...
    copy .env.example .env
)

REM Change directory to the source code folder
cd src

REM Ask whether to run makemigrations (default No)
set /p RUN_MIGRATIONS="Do you want to run makemigrations? [y/N]: "
if /i "%RUN_MIGRATIONS%"=="" set RUN_MIGRATIONS=N
if /i "%RUN_MIGRATIONS%"=="Y" (
    python manage.py makemigrations common
    python manage.py makemigrations authentication
    python manage.py makemigrations mail
    python manage.py makemigrations celery_tasks
    python manage.py makemigrations upload
)

REM Ask whether to run migrate (default Yes)
set /p RUN_MIGRATE="Do you want to run migrate? [Y/n]: "
if /i "%RUN_MIGRATE%"=="" set RUN_MIGRATE=Y
if /i "%RUN_MIGRATE%"=="Y" (
    python manage.py migrate
)

REM Ask whether to create superuser (default No)
set /p CREATE_SUPERUSER="Do you want to create a superuser? [y/N]: "
if /i "%CREATE_SUPERUSER%"=="" set CREATE_SUPERUSER=N
if /i "%CREATE_SUPERUSER%"=="Y" (
    python manage.py createsuperuser
)

REM Ask for server port
set /p PORT="> Server port (default 80): "
if "%PORT%"=="" set PORT=80

REM Start Django server
python manage.py runserver 0.0.0.0:%PORT%
