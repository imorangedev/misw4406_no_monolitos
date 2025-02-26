import json
import zipfile

from base_command import Comand, ComandHandler


class JsonToZip(Comand):
    def __init__(self, destinationPath: str, jsonObject: str):
        super().__init__()
        self.destinationPath = destinationPath
        self.jsonObject = jsonObject

    def json_to_zip(self, jsonObject: str, destinationPath: str) -> str:
        
        try:

            with zipfile.ZipFile(destinationPath, mode="w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zip_file: 
                # Dump JSON data
                dumped_JSON: str = json.dumps(jsonObject, ensure_ascii=False, indent=4)
                # Write the JSON data into `data.json` *inside* the ZIP file
                zip_file.writestr("data.json", data=dumped_JSON)
                # Test integrity of compressed archive
                zip_file.testzip()

        except Exception as e:
            print(e)
            return False

class JsonToZipHandler(ComandHandler):
    def handle(self, comand: JsonToZip):
        return comand.json_to_zip(comand.jsonObject, comand.destinationPath)