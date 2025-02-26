import json
import base64
from google.cloud import storage

from base_command import Comand, ComandHandler


class GetImage(Comand):
    def __init__(self, image_id: str):
        self.image_name = image_id
        self.bucket_name = "experimento_misw4406"


    def get_image(self, image_id: str, bucket_name: str) -> str:

        try:
            storage_client = storage.Client.create_anonymous_client()
            bucket = storage_client.bucket(bucket_name)
            blob = bucket.blob(f'repo_imagenes/{str(image_id)}.jpg')
            image_bytes = blob.download_as_bytes()
            image_byase64 = base64.b64encode(image_bytes).decode("utf-8")
            image_json = json.dumps({"image": image_byase64})
            return image_json

        except Exception as e:
            print(e)
            return False
        
class GetImageHandler(ComandHandler):
    def handle(self, comand: GetImage):
        return comand.get_image(comand.image_name, comand.bucket_name)
    
if __name__ == '__main__':
    import sys
    image_id = 1
    comand = GetImage(image_id)
    handler = GetImageHandler()
    print(handler.handle(comand))