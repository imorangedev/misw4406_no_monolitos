import json
import zipfile
from io import BytesIO
from google.cloud import storage

# from base_comand import Comand, ComandHandler


class JsonToZip():
    def __init__(self, jsonObjects: list, zip_name: str):
        super().__init__()
        self.jsonObjects = jsonObjects
        self.zip_name = zip_name
        self.bucket_name = "monolitos_misw4406"
        self.destination_blob_name = "repo_zip"

    def json_to_zip(self, jsonObjects: list, zip_name: str) -> str:
        
        try:
            zip_buffer = BytesIO()

            with zipfile.ZipFile(zip_buffer, mode="w",
                                 compression=zipfile.ZIP_DEFLATED,
                                 compresslevel=9) as zip_file:
                
                for index, json_obj in enumerate(jsonObjects):

                    
                    dumped_JSON: str = json.dumps(json_obj, ensure_ascii=False, indent=4)
                    json_dict = json.loads(json_obj)
                    json_file_name = json_dict['filename']
                    zip_file.writestr(json_file_name, data=dumped_JSON)

                
            zip_buffer.seek(0)


            storage_client = storage.Client()
            bucket = storage_client.bucket(self.bucket_name)
            blob = bucket.blob(f'{self.destination_blob_name}/{zip_name}.zip')
            blob.upload_from_file(zip_buffer, content_type="application/zip")

            print(f"ZIP file successfully uploaded to gs://{self.bucket_name}/{self.destination_blob_name}")
            return True


        except Exception as e:
            print(e)
            return False

class JsonToZipHandler():
    def handle(self, comand: JsonToZip):
        return comand.json_to_zip(comand.jsonObjects, comand.zip_name)