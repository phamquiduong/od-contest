@echo off

@REM Cài đặt biến môi trường cho Django
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

@REM Nâng cấp pip
python -m pip install --upgrade pip

@REM Cài đặt các gói Python
pip install -r requirements.txt
cls

@REM Tiến hành chạy Worker
cd src
celery -A main worker -l info --pool=solo -Q email_queue
