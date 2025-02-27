from pathlib import Path

import google.generativeai as genai
from dotenv import dotenv_values
from PIL import Image

SCREENSHOT_PATH = "./screenshot.png"


class ImageTranslator:
    def __init__(self) -> None:
        self.config = dotenv_values()
        genai.configure(api_key=self.config.get("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel("gemini-2.0-flash")

    def generate_content(self, imege_path: str) -> str:
        image = Image.open(Path(imege_path))
        prompt = "画像の文言が日本語の場合は、そのまま文字起こしをしてください。日本語以外の場合は日本語に翻訳して出力してください。"

        response = self.model.generate_content([prompt, image])

        if response.text:
            return response.text
        else:
            return "No content generated."


if __name__ == "__main__":
    translator = ImageTranslator()
    content = translator.generate_content(SCREENSHOT_PATH)
    print(content)
