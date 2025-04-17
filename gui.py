from pathlib import Path

import customtkinter as ctk
import pyperclip

import image_translator
import screen_capture
import settings

CAPTURE_PATH = Path.cwd() / "capture.png"  # キャプチャ画像の保存先パス
ENV_PATH = Path.cwd() / ".env"  # 設定ファイルのパス

# 表示フォント
FONT_PATH = Path.cwd() / "UDEVGothicJPDOC-Regular.ttf"  # ファイルパス
FONT_TYPE = "UDEV Gothic JPDOC Regular"  # フォントタイプ
FONT_SIZE = 14  # フォントサイズ


class CaptureAndTranslateGUI(ctk.CTk):
    """キャプチャ結果を表示するダイアログクラス

    Args:
        ctk (_type_): customtkinterのCTkクラスを継承
    """
    def __init__(self, text: str):
        """コンストラクタ

        Args:
            text (str): 表示するテキスト
        """
        super().__init__()
        ctk.FontManager.load_font(FONT_PATH.as_posix())  # フォントを読み込む

        self.text = text

        # フォームのセットアップをする
        self.setup_form(self.text)

    def setup_form(self, text: str) -> None:
        """キャプチャ結果を表示するダイアログを表示する

        Args:
            text (str): 表示するキャプチャ結果のテキスト
        """
        ctk.set_appearance_mode("System")  # 外観モードを設定
        ctk.set_default_color_theme("blue")  # カラーテーマを設定

        # フォームサイズ設定
        self.geometry("800x600")
        self.title("Capture and Translate")

        text_area = ctk.CTkTextbox(
            master=self, font=ctk.CTkFont(family=FONT_TYPE, size=FONT_SIZE), wrap="word"
        )  # CTkTextboxを使用
        text_area.insert("1.0", text)  # テキストを挿入
        text_area.pack(expand=True, fill="both")

    def click_close(self) -> None:
        """イベントハンドラ: ウィンドウを閉じるボタンがクリックされた"""
        self.destroy()


def main() -> None:
    """メイン関数"""
    # 設定ファイルが存在しない場合、Settingsを表示して終了する
    if not ENV_PATH.exists():
        settings.main()
        return

    # 画面をキャプチャする
    screen_capture.main(CAPTURE_PATH)
    if not CAPTURE_PATH.exists():
        return

    # キャプチャ画像を文字起こしする
    text = image_translator.main(CAPTURE_PATH)
    pyperclip.copy(text)

    # キャプチャ結果を表示する
    app = CaptureAndTranslateGUI(text)
    app.mainloop()


if __name__ == "__main__":
    main()
