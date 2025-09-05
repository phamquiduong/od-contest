@echo off

@REM Cài đặt biến môi trường
call .\setup_env.bat

@REM Nâng cấp pip
python -m pip install --upgrade pip

@REM Cài đặt requirements
pip install -r requirements.txt
cls

@REM Cài đặt cổng để chạy server Django
set /p PORT="> Server port (default 80): "
if "%PORT%"=="" set PORT=80
cls

@REM Tiến hành chạy server Django
cd src
python manage.py runserver 0.0.0.0:%PORT%
