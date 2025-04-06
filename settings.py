from pathlib import Path
from tkinter import messagebox

import customtkinter as ctk
from dotenv import load_dotenv, set_key

ENV_PATH = Path.cwd() / ".env"  # 設定ファイルのパス

# 表示フォント
FONT_PATH = Path.cwd() / "UDEVGothicJPDOC-Regular.ttf"  # ファイルパス
FONT_TYPE = "UDEV Gothic JPDOC Regular"  # フォントタイプ
FONT_SIZE = 14  # フォントサイズ


class SettingsApp(ctk.CTk):
    def __init__(self):
        """コンストラクタ"""
        super().__init__()
        ctk.FontManager.load_font(FONT_PATH.as_posix())  # フォントを読み込む

        # フォームのセットアップをする
        self.setup_form(self.text)

    def setup_form(self, text: str) -> None:
        ctk.set_appearance_mode("System")  # 外観モードを設定
        ctk.set_default_color_theme("blue")  # カラーテーマを設定

        # フォームサイズ設定
        self.geometry("450x230")  # ウィンドウのサイズを設定 (幅x高さ)
        self.title("Settings")

        # APIキー入力フィールドの設定
        self.label_api_key = ctk.CTkLabel(
            master=self,
            text="Google AI Studioで生成したAPI Keyを入力してください",
            font=ctk.CTkFont(family=FONT_TYPE, size=FONT_SIZE),
        )
        self.label_api_key.pack(pady=10)
        self.entry_api_key = ctk.CTkEntry(
            master=self,
            placeholder_text="API Key",
            font=ctk.CTkFont(family=FONT_TYPE, size=FONT_SIZE),
            width=350,
        )
        self.entry_api_key.pack()

        # ドロップダウンリストの設定
        self.label_display_scale = ctk.CTkLabel(
            master=self,
            text="Windowsの表示スケールを選択してください",
            font=ctk.CTkFont(family=FONT_TYPE, size=FONT_SIZE),
        )
        self.label_display_scale.pack(pady=10)
        self.display_scale_combobox = ctk.CTkComboBox(
            master=self,
            values=["100%", "125%", "150%"],
            state="readonly",
            font=ctk.CTkFont(family=FONT_TYPE, size=FONT_SIZE),
        )
        self.display_scale_combobox.pack()
        self.display_scale_combobox.set("100%")

        self.button_submit = ctk.CTkButton(
            master=self,
            text="設定します",
            command=self.on_submit,
            font=ctk.CTkFont(family=FONT_TYPE, size=FONT_SIZE),
        )
        self.button_submit.pack(pady=20)

    def on_submit(self) -> None:
        """イベントハンドラ: 設定ボタンがクリックされた"""
        gemini_api_key = self.entry_api_key.get()
        if not gemini_api_key:
            messagebox.showerror("Error", "API Keyが入力されていません")
            return

        display_scale_mapping = {"100%": "100", "125%": "125", "150%": "150"}
        display_scale = display_scale_mapping.get(
            self.display_scale_combobox.get(), "100"
        )  # デフォルトは "100"

        # .envファイルに書き込み
        set_key(ENV_PATH, "GEMINI_API_KEY", gemini_api_key)
        set_key(ENV_PATH, "DISPLAY_SCALE", display_scale)

        # 完了メッセージ
        messagebox.showinfo(
            "Completed", "設定が完了しました。次回の起動から反映されます"
        )
        self.destroy()


def main() -> None:
    """メイン関数"""
    app = SettingsApp()
    app.mainloop()


if __name__ == "__main__":
    main()
