@echo off

cd docker

if not exist ".env" (
    echo Copying .env.example to .env...
    copy .env.example .env
)

docker-compose down

docker-compose up --build -d
