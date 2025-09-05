@echo off

@REM Cài đặt biến môi trường
call .\setup_env.bat

@REM Cài đặt các gói Python
call .\setup_pip.bat
cls

@REM Tiến hành chạy migrate
cd src
python manage.py migrate
