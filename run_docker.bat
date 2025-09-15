@echo off
setlocal enabledelayedexpansion


@REM Set up environment variables for Django
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


@REM Start working with docker compose
cd docker


@REM Set up environment variables for Docker
if not exist ".env" (
    echo Copying .env.example to .env...
    copy .env.example .env

    echo.
    echo Please open "docker/.env" and update the configuration for docker compose.
    echo After making the necessary changes, press ENTER to continue...
    pause >nul

    cls
)


@REM Shut down old docker containers
docker-compose --profile * down
cls


@REM Generate Alertmanager config file
cd alertmanager
python render_alertmanager.py
echo Rendered Alertmanager config file successfully...
cd ..


@REM Build and start docker compose in the background
set CMD=


set /p srv="Start server [Y/n]? "
if "!srv!"=="" set srv=Y
if /i "!srv!"=="Y" set CMD=!CMD! --profile server


set /p db="Start database [Y/n]? "
if "!db!"=="" set db=Y
if /i "!db!"=="Y" set CMD=!CMD! --profile database


set /p cel="Start celery [y/N]? "
if "!cel!"=="" set cel=N
if /i "!cel!"=="Y" set CMD=!CMD! --profile celery


set /p mon="Start monitoring [y/N]? "
if "!mon!"=="" set mon=N
if /i "!mon!"=="Y" set CMD=!CMD! --profile monitor


if "!CMD!"=="" (
    echo No services selected. Exiting...
    exit /b
)


cls


@REM Show selected services before starting
echo Starting docker compose with:
echo    !CMD!
echo.


@REM Start docker compose with chosen profiles
docker-compose !CMD! up --build -d
