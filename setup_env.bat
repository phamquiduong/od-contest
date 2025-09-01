@echo off

IF NOT EXIST ".env" (
    echo .env not found. Copying from .env.example...
    copy .env.example .env
) ELSE (
    echo .env already exists. Skipping copy.
)
