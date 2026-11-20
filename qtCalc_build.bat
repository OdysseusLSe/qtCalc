@echo off
::
:: This Script creates qtCalc.exe file in windows
:: You need a "python install manager installed: https://www.python.org/downloads/
:: and a pyhton 3.15 verion installed to run this script
::
set PYTHON_MANAGER_DEFAULT=3.15
set ADDITIONAL_PARAMETERS=--onefile --noconsole --icon=./icons/icon.ico --add-data "./icons/icon.ico;./icons/."
:: Uncomment the following line if you want to make an exe with a console window for debuggung purpos:
::set ADDITIONAL_PARAMETERS=--onefile --icon=./icons/icon.ico --add-data "./icons/icon.ico;./icons/."
:: Now install a virtual environment with the needed requirments and build an exe file
:: If venv2 is already there the previously generated exe ist directly called
if exist "venv\" (
  REM Nothing to do
) else (
  python -m venv venv
  venv\Scripts\pip install -r requirements.txt
)
venv\Scripts\pip install -U pyinstaller
venv\Scripts\pyinstaller %ADDITIONAL_PARAMETERS% main.py
copy .\dist\main.exe qtCalc.exe
qtCalc.exe