@echo off
:: Script to install a virtual environment with the needed requirments and start qtFractal
set PYTHON_MANAGER_DEFAULT=3.15
if exist "venv\" (
  REM Nothing to do
) else (
  python -m venv venv
  venv\Scripts\pip install -r requirements.txt
)
venv\Scripts\python.exe main.py %*
