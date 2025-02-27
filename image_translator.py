from pathlib import Path

import google.generativeai as genai
from dotenv import dotenv_values
from PIL import Image

SCREENSHOT_PATH = Path("./screenshot.png")

config = dotenv_values()
genai.configure(api_key=config.get("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

image = Image.open(SCREENSHOT_PATH)
prompt = "画像の文言が日本語の場合は、そのまま文字起こしをしてください。日本語以外の場合は日本語に翻訳して出力してください。"

response = model.generate_content([prompt, image])

# 結果を出力
if response.text:
    print(response.text)
else:
    print("No content generated.")
