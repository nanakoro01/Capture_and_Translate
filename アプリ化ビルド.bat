@echo off
python -m venv --upgrade-deps .venv
call .venv\Scripts\activate
pyinstaller gui.py -y --noconsole --clean -n Capture_and_Translate
pause