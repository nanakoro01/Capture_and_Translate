# Capture and Translate
画面をキャプチャして、文字起こし（翻訳や要約なども）を行う
## 環境の構築方法
- 開発時のPythonのバージョン: 3.12.8
- 環境構築.batをダブルクリック
## 実行用ショートカットの作り方
- `Capture and Translate.bat`からショートカットファイルを作成する
- ショートカットのプロパティを開き、以下を変更する
    - 実行時の大きさ: 最小化
    - アイコンの変更: %SystemRoot%\System32\SHELL32.dllから適当に
## 使用方法
- 初回実行時には設定ダイアログが開くので、以下を選択する
    - Google API Studioで取得したAPIキー
    - Windowsの表示スケール（4Kディスプレイの場合は150、それ以外の場合は100）
- 2回目以降は画面が薄白くなるので、取り込みたい範囲をマウスで範囲選択する
- しばらくすると文字起こし結果が表示する
    - 日本語以外の場合は翻訳して表示する
## 使っているパッケージ
- customtkinter 5.2.2 (pip install customtkinter)
- google-generativeai 0.8.4 (pip install google-generativeai)
- pillow 11.1.0 (pip install pillow)
- pyperclip 1.9.0 (pip install pyperclip)
- python-dotenv 1.1.0 (pip install customtkinter)
