@echo off

@REM Nâng cấp pip
python -m pip install --upgrade pip

@REM Cài đặt requirements chính
pip install -r requirements.txt

@REM Cài đặt requirements cho môi trường dev
pip install -r requirements.dev.txt
