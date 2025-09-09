@echo off
setlocal enabledelayedexpansion

@REM Cài đặt biến môi trường cho Django
if not exist ".env.docker" (
    echo Copying .env.example to .env.docker...
    copy .env.example .env.docker
    cls

    echo.
    echo Please open ".env.docker" and update the configuration to match your Docker setup.
    echo After making the necessary changes, press ENTER to continue...
    pause >nul

    cls
)

@REM Bắt đầu thao tác với docker compose
cd docker

@REM Cài đặt biến môi trường cho Docker
if not exist ".env" (
    echo Copying .env.example to .env...
    copy .env.example .env

    echo.
    echo Please open "docker/.env" and update the configuration for docker compose.
    echo After making the necessary changes, press ENTER to continue...
    pause >nul

    cls
)

@REM Tạo file config alert manager
cd alertmanager
python render_alertmanager.py
echo Rendered Alertmanager config file successfully...
cd ..

@REM Tắt các docker container cũ
docker-compose --profile * down
cls

@REM Build và bật docker compose dưới nền
set CMD=

set /p srv="Start server profile [Y/n]? "
if "!srv!"=="" set srv=Y
if /i "!srv!"=="Y" set CMD=!CMD! --profile server

set /p db="Start database profile [Y/n]? "
if "!db!"=="" set db=Y
if /i "!db!"=="Y" set CMD=!CMD! --profile database

set /p cel="Start celery profile [Y/n]? "
if "!cel!"=="" set cel=Y
if /i "!cel!"=="Y" set CMD=!CMD! --profile celery

set /p mon="Start monitoring profile [y/N]? "
if "!mon!"=="" set mon=N
if /i "!mon!"=="Y" set CMD=!CMD! --profile monitor

if "!CMD!"=="" (
    echo No profiles selected. Exiting...
    exit /b
)

cls

docker-compose !CMD! up --build -d
