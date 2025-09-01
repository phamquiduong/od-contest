@echo off

call setup_env.bat

call run_pip_install.bat
cls

pytest -v src
