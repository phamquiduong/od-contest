@echo off

cd docker

@REM Cài đặt biến môi trường
if not exist ".env" (
    echo Copying .env.example to .env...
    copy .env.example .env
)

@REM Tắt các docker container cũ
docker-compose down

@REM Build và bật docker compose dưới nền
docker-compose up --build -d
