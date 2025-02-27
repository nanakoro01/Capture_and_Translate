@echo off
python -m venv --upgrade-deps .venv
call .venv\Scripts\activate
echo キャプチャして文字起こしを開始します
echo このウィンドウが邪魔にならないようにしてから
pause
python gui.py
