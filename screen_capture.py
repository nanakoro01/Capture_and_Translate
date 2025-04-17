import tkinter as tk
from pathlib import Path
from tkinter import Canvas, Tk, messagebox

from dotenv import dotenv_values
from PIL import ImageGrab


class ScreenCaptureApp:
    """スクリーンキャプチャアプリケーションのクラス

    Attributes:
        root (Tk): Tkinterのルートウィンドウ
        canvas (Canvas): 描画用のキャンバス
        start_x (int): マウスドラッグ開始時のX座標
        start_y (int): マウスドラッグ開始時のY座標
        rect (int): 描画された矩形のID
    """

    capture_path = default_capture_path = Path.cwd() / "capture.png"

    def __init__(self, root: Tk, capture_path: Path = default_capture_path) -> None:
        """コンストラクタ

        Args:
            root (Tk): Tkinterのルートウィンドウ
            capture_path (str): 画像の保存パス
        """
        # 表示スケールを取得する
        self.config = dotenv_values()
        self.display_scale = float(self.config.get("DISPLAY_SCALE", 100)) / 100.0

        # キャプチャ対象の画像を作成する
        self.root: Tk = root
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-alpha", 0.3)
        self.canvas: Canvas = tk.Canvas(root, cursor="cross")
        self.canvas.pack(fill=tk.BOTH, expand=tk.YES)
        self.start_x: int
        self.start_y: int
        self.rect: int
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)
        self.root.bind("<Escape>", self.on_escape)  # Escキーのバインド

        self.capture_path = capture_path

    def on_button_press(self, event: tk.Event) -> None:
        """マウスボタンが押された時のイベントハンドラ

        Args:
            event (tk.Event): Tkinterのイベントオブジェクト
        """
        self.start_x = event.x
        self.start_y = event.y
        self.rect = self.canvas.create_rectangle(
            self.start_x, self.start_y, self.start_x, self.start_y, outline="red"
        )

    def on_mouse_drag(self, event: tk.Event) -> None:
        """マウスドラッグ時のイベントハンドラ

        Args:
            event (tk.Event): Tkinterのイベントオブジェクト
        """
        cur_x, cur_y = (event.x, event.y)
        self.canvas.coords(self.rect, self.start_x, self.start_y, cur_x, cur_y)

    def on_button_release(self, event: tk.Event) -> None:
        """マウスボタンが離された時のイベントハンドラ

        Args:
            event (tk.Event): Tkinterのイベントオブジェクト
        """
        end_x, end_y = (event.x, event.y)
        x1 = min(self.start_x, end_x)
        y1 = min(self.start_y, end_y)
        x2 = max(self.start_x, end_x)
        y2 = max(self.start_y, end_y)

        if (x2 - x1) < 50 or (y2 - y1) < 50:
            messagebox.showwarning(
                "警告", "選択範囲が小さすぎます。もう一度やり直してください。"
            )
            self.canvas.delete(self.rect)
            self.root.deiconify()
        else:
            self.root.withdraw()
            self.capture_and_save(x1, y1, x2, y2)
            self.root.destroy()

    def on_escape(self, event: tk.Event) -> None:
        """Escキーが押された時のイベントハンドラ

        Args:
            event (tk.Event): Tkinterのイベントオブジェクト
        """
        messagebox.showwarning("警告", "選択作業がキャンセルされました。")
        if self.capture_path.exists():
            self.capture_path.unlink()
        self.root.destroy()

    def capture_and_save(self, x1: int, y1: int, x2: int, y2: int) -> None:
        """スクリーンキャプチャを行い、画像を保存する

        Args:
            x1 (int): 矩形の左上のX座標
            y1 (int): 矩形の左上のY座標
            x2 (int): 矩形の右下のX座標
            y2 (int): 矩形の右下のY座標
        """
        # スケールに応じて座標を調整
        x1_scaled = int(x1 * self.display_scale)
        y1_scaled = int(y1 * self.display_scale)
        x2_scaled = int(x2 * self.display_scale)
        y2_scaled = int(y2 * self.display_scale)

        img = ImageGrab.grab(bbox=(x1_scaled, y1_scaled, x2_scaled, y2_scaled))
        img.save(Path(self.capture_path))


def main(capture_path: Path = ScreenCaptureApp.default_capture_path) -> None:
    """メイン処理"""
    root = tk.Tk()
    ScreenCaptureApp(root, capture_path)
    root.mainloop()


if __name__ == "__main__":
    main()
