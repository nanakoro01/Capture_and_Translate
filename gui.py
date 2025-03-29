import sys
import tkinter as tk
from pathlib import Path

import pyperclip

import image_translator
import screen_capture
import settings


class CaptureAndTranslateGUI:
    def __init__(self):
        self.CAPTURE_PATH = Path.cwd() / "capture.png"  # キャプチャ画像の保存先パス
        self.ENV_PATH = Path.cwd() / ".env"  # 設定ファイルのパス

        # 設定ファイルの存在チェック
        if not self.ENV_PATH.exists():
            settings.main()
            sys.exit()

    def click_close(self) -> None:
        """イベントハンドラ: ウィンドウを閉じるボタンがクリックされた"""
        sys.exit()

    def show_text_dialog(self, text: str) -> None:
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

        dialog.protocol(
            "WM_DELETE_WINDOW", self.click_close
        )  # ウィンドウを閉じるボタンのイベントハンドラを設定

        dialog.mainloop()

    def main(self):
        screen_capture.main(self.CAPTURE_PATH)
        if not self.CAPTURE_PATH.exists():
            sys.exit()
        text = image_translator.main(self.CAPTURE_PATH)
        pyperclip.copy(text)
        self.show_text_dialog(text)


if __name__ == "__main__":
    app = CaptureAndTranslateGUI()
    app.main()
