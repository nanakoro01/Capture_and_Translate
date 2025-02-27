import tkinter as tk

import image_translator
import screen_capture

SCREENSHOT_PATH = "./screenshot.png"


def show_text_dialog(text: str) -> None:
    dialog = tk.Tk()
    dialog.title("キャプチャ結果")

    text_area = tk.Text(dialog, wrap="word")
    text_area.pack(expand=True, fill="both")

    text_area.insert("1.0", text)
    text_area.config(state="disabled")

    dialog.protocol("WM_DELETE_WINDOW", dialog.destroy)

    dialog.mainloop()


if __name__ == "__main__":
    screen_capture.main()
    print("読み取り中。ちょっと待ってね‥")
    text = image_translator.main()
    show_text_dialog(text)
