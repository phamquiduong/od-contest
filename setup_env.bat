@echo off

@REM Copy file .env.example thành .env nếu file .env không tồn tại
if not exist ".env" (
    echo Copying .env.example to .env...
    copy .env.example .env
)
