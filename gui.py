import tkinter as tk

import image_translator
import screen_capture

SCREENSHOT_PATH = "./screenshot.png"


def click_close() -> None:
    print("終了処理中。ちょっと待ってね‥")
    exit()


def show_text_dialog(text: str) -> None:
    dialog = tk.Tk()
    dialog.title("キャプチャ結果")

    text_area = tk.Text(dialog, wrap="word")
    text_area.pack(expand=True, fill="both")

    text_area.insert("1.0", text)
    text_area.config(state="normal")

    dialog.protocol("WM_DELETE_WINDOW", click_close)

    dialog.mainloop()


if __name__ == "__main__":
    print("キャプチャの準備をしています。カーソルが十字カーソルになるまでまってね‥")
    screen_capture.main()
    print("キャプチャ結果を分析中。ちょっと待ってね‥")
    text = image_translator.main()
    show_text_dialog(text)
