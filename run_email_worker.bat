@echo off


@REM Set up environment variables for Django
if not exist ".env" (
    echo Copying .env.example to .env...
    copy .env.example .env
    cls

    echo.
    echo Please open ".env" and update the configuration for your Django project.
    echo After making the necessary changes, press ENTER to continue...
    pause >nul

    cls
)


@REM Upgrade pip
python -m pip install --upgrade pip


@REM Install Python packages
pip install -r requirements.txt
cls


@REM Start Celery Worker
cd src
celery -A main worker -l info --pool=solo -Q email_queue
