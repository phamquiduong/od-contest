@echo off

@REM Cài đặt biến môi trường
call .\setup_env.bat

@REM Cài đặt các gói Python
call .\setup_pip.bat
cls

@REM Cài đặt cổng để chạy server Celery Flower
set /p FLOWER_PORT="> Flower port (default 5555): "
if "%FLOWER_PORT%"=="" set FLOWER_PORT=5555
cls

@REM Tiến hành chạy Flower
cd src
celery -A main flower --port=%FLOWER_PORT%
