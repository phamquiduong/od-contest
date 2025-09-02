@echo off

@REM Cài đặt biến môi trường
call setup_env.bat

@REM Cài đặt các gói Python
call run_pip_install.bat
cls

@REM Tiến hành chạy testing
pytest -v src
