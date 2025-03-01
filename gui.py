import tkinter as tk
from pathlib import Path

import image_translator
import screen_capture
import settings

CAPTURE_PATH = Path.cwd() / "capture.png"  # キャプチャ画像の保存先パス
ENV_PATH = Path.cwd() / ".env"  # 設定ファイルのパス

# 設定ファイルの存在チェック
if not ENV_PATH.exists():
    settings.main()
    exit()


def click_close() -> None:
    """イベントハンドラ: ウィンドウを閉じるボタンがクリックされた"""
    exit()


def show_text_dialog(text: str) -> None:
    """キャプチャ結果を表示するダイアログを表示する

    Args:
        text (str): 表示するキャプチャ結果のテキスト
    """
    dialog = tk.Tk()
    dialog.title("キャプチャ結果")

    text_area = tk.Text(dialog, wrap="word")
    text_area.pack(expand=True, fill="both")

    text_area.insert("1.0", text)
    text_area.config(state="normal")

    dialog.protocol("WM_DELETE_WINDOW", click_close)  # ウィンドウを閉じるボタンのイベントハンドラを設定

    dialog.mainloop()


if __name__ == "__main__":
    screen_capture.main(CAPTURE_PATH)
    text = image_translator.main(CAPTURE_PATH)
    show_text_dialog(text)
