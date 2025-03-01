import tkinter as tk
from pathlib import Path
from tkinter import messagebox, ttk

from dotenv import load_dotenv, set_key


class SettingsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Settings")
        self.root.geometry("350x230")  # ウィンドウのサイズを設定 (幅x高さ)

        # .envファイルのパス
        self.env_path = Path.cwd() / ".env"

        # .envファイルを読み込み
        if self.env_path.exists():
            load_dotenv(self.env_path)

        # APIキー入力フィールドの設定
        self.label_api_key = tk.Label(
            root, text="Google AI Studioで生成したAPI Keyを入力してください"
        )
        self.label_api_key.pack(pady=10)
        self.api_key_var = tk.StringVar()
        self.entry_api_key = tk.Entry(root, textvariable=self.api_key_var, width=50)
        self.entry_api_key.pack(pady=10)

        # ドロップダウンリストの設定
        self.label_display_scale = tk.Label(
            root, text="Windowsの表示スケールを選択してください"
        )
        self.label_display_scale.pack(pady=10)
        self.display_scale_var = tk.StringVar()
        self.display_scale_combobox = ttk.Combobox(
            root, textvariable=self.display_scale_var, state="readonly"
        )
        self.display_scale_combobox["values"] = ("100%", "125%", "150%")
        self.display_scale_combobox.pack(pady=10)
        self.display_scale_combobox.current(0)  # デフォルト値を設定

        self.button_submit = tk.Button(root, text="OK", command=self.on_submit)
        self.button_submit.pack(pady=10)

    def on_submit(self):
        """設定を保存してウィンドウを閉じる"""
        gemini_api_key = self.api_key_var.get()
        display_scale_mapping = {"100%": "100", "125%": "125", "150%": "150"}
        display_scale = display_scale_mapping.get(
            self.display_scale_var.get(), "100"
        )  # デフォルトは "100"

        # .envファイルに書き込み
        if gemini_api_key:
            set_key(self.env_path, "GEMINI_API_KEY", gemini_api_key)
        if display_scale:
            set_key(self.env_path, "DISPLAY_SCALE", display_scale)

        # 完了メッセージ
        messagebox.showinfo(
            "Completed", "設定が完了しました。次回の起動から反映されます"
        )
        self.root.quit()


def main():
    root = tk.Tk()
    app = SettingsApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
