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


@REM Install requirements
pip install -r requirements.txt
cls


@REM Change dir to folder source code
cd src


@REM Run migrations
python manage.py migrate


@REM Set port to run Django server
set /p PORT="> Server port (default 80): "
if "%PORT%"=="" set PORT=80
cls


@REM Start Django server
python manage.py runserver 0.0.0.0:%PORT%
