# Capture_and_Translate
画面をキャプチャして、文字起こし（翻訳や要約なども）を行う
## 環境の構築方法
- 開発時のPythonのバージョン: 3.12.8
- 環境構築.batをダブルクリック
- カレントディレクトリに`.env`ファイルを作成する。設定値は以下の通り
    ```
    GEMINI_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    DISPLAY_SCALE=150
    ```
    - `GEMINI_API_KEY`: Google API Studioで取得したAPIキー
    - `DISPLAY_SCALE`: Windowsの表示スケール
        - 通常は`100`、4Kの場合は`150`
