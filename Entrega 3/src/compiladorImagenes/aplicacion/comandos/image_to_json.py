import base64
from io import BytesIO
from PIL import Image

from base_command import Comand, ComandHandler


class ImageToJson(Comand):
    def __init__(self, filepath: str):
        self.filepath = filepath

    def image_to_json(self, filepath: str) -> str:

        try:
            png_image = Image.open(filepath)
            jpg_buffer = BytesIO()
            png_image.save(jpg_buffer, format="PNG")
            enc_data = base64.b64encode(jpg_buffer.getvalue()).decode("utf-8")
            return enc_data
        
        except Exception as e:
            print(e)
            return False

class ImageToJsonHandler(ComandHandler):
    def handle(self, comand: ImageToJson):
        return comand.image_to_json(comand.filepath)
    