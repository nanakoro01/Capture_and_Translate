# Capture_and_Translate
画面をキャプチャして、文字起こし（翻訳や要約なども）を行う
## 環境の構築方法
- 開発時のPythonのバージョン: 3.12.8
- 環境構築.batをダブルクリック
## Pyinstallerを使ったアプリ化の手順
- アプリ化ビルド.batをダブルクリック
- `dist/Capture_and_Translate`フォルダに`Capture_and_Translate.exe`が作られるので、ショートカットをスタートメニューに配置するとか、タスクバーに登録するとか、あとはご自由に
## 使用方法
- 初回実行時には設定ダイアログが開くので、以下を選択する
    - Google API Studioで取得したAPIキー
    - Windowsの表示スケール（4Kディスプレイの場合は150、それ以外の場合は100）
- 2回目以降は画面が薄白くなるので、取り込みたい範囲をマウスで範囲選択する
- しばらくすると文字起こし結果が表示する
    - 日本語以外の場合は翻訳して表示する
## 使っているパッケージ
- google-generativeai 0.8.4
- pillow 11.1.0
- pyperclip 1.9.0
- python-dotenv 1.1.0