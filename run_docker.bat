@echo off
REM ==============================================
REM Docker Setup Script with Django Setup
REM ==============================================

REM Set up environment variables
if not exist ".env" (
    echo Copying .env.example to .env...
    copy .env.example .env
)

REM Change directory to the docker folder
cd docker

REM Stop all Docker containers and remove orphans
echo Stopping all Docker containers and removing orphans...
docker-compose --env-file ../.env --profile * down

REM Start main Docker containers
echo Starting main Docker containers...
docker-compose --env-file ../.env up --build -d

REM Ask whether to start monitoring services (default No)
set /p START_MONITORING="Do you want to start monitoring services? [y/N]: "
if /i "%START_MONITORING%"=="" set START_MONITORING=N
if /i "%START_MONITORING%"=="Y" (
    echo Starting Docker containers with monitoring profile...
    docker-compose --env-file ../.env --profile monitoring up --build -d
)
