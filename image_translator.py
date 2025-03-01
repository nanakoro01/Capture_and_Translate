from pathlib import Path

import google.generativeai as genai
from dotenv import dotenv_values
from PIL import Image


class ImageTranslator:
    """画像翻訳を行うクラス。

    Attributes:
        config (dict): 設定情報の辞書
        model (genai.GenerativeModel): GenerativeModelオブジェクト
        capture_path (Path): キャプチャ画像のパス
    """
    capture_path = default_capture_path = Path.cwd() / "capture.png"

    def __init__(self, capture_path: Path = default_capture_path) -> None:
        self.config = dotenv_values()
        genai.configure(api_key=self.config.get("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel("gemini-2.0-flash")

        self.capture_path = capture_path

    def generate_content(self) -> str:
        """Geminiで画像認識を行う

        Returns:
            str: 画像認識結果のテキスト
        """
        image = Image.open(self.capture_path)
        prompt = "画像の文言が日本語の場合は、そのまま文字起こしをしてください。日本語以外の場合は日本語に翻訳して出力してください。"

        response = self.model.generate_content([prompt, image])

        if response.text:
            return response.text
        else:
            return "No content generated."


def main(capture_path: Path = ImageTranslator.default_capture_path) -> str:
    """Geminiで画像認識を行う

    Args:
        capture_path (Path, optional): キャプチャ画像のパス

    Returns:
        str: 画像認識結果のテキスト
    """
    if not capture_path.exists():
        raise FileNotFoundError(f"キャプチャ画像が見つかりません: {capture_path}")
    translator = ImageTranslator(capture_path)
    return translator.generate_content()


if __name__ == "__main__":
    main()
