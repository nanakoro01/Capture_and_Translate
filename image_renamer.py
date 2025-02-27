import os

from PIL import Image
from PIL.ExifTags import TAGS


class ImageRenamer:
    def __init__(self, directory: str) -> None:
        """ImageRenamerのコンストラクタ。

        Args:
            directory (str): 画像ファイルが含まれるディレクトリのパス。
        """
        self.directory = directory

    def get_exif_date_taken(self, image_path: str) -> str:
        """画像のEXIFデータから撮影日時を取得する関数。

        Args:
            image_path (str): 画像ファイルのパス。

        Returns:
            str: 撮影日時を表す文字列。取得できない場合はNone。
        """
        with Image.open(image_path) as image:
            exif_data = image._getexif()
            if exif_data:
                for tag, value in exif_data.items():
                    decoded = TAGS.get(tag, tag)
                    if decoded == "DateTimeOriginal":
                        return value.replace(":", "").replace(" ", "_")
        return None

    def rename_images(self) -> None:
        """ディレクトリ内の画像ファイルを撮影日時に基づいてリネームする関数。"""
        for filename in os.listdir(self.directory):
            if filename.lower().endswith((".jpg", ".jpeg", ".png")):
                file_path = os.path.join(self.directory, filename)
                date_taken = self.get_exif_date_taken(file_path)
                if date_taken:
                    new_filename = f"{date_taken}{os.path.splitext(filename)[1]}"
                    new_file_path = os.path.join(self.directory, new_filename)
                    os.rename(file_path, new_file_path)
                    print(f"Renamed {file_path} to {new_file_path}")


if __name__ == "__main__":
    directory = r"C:\0\Work\GReeeeN _遥か_卒業パーティーEdit\photo"
    renamer = ImageRenamer(directory)
    renamer.rename_images()
