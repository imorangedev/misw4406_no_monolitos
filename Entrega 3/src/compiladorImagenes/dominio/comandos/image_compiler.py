from uuid import uuid4

from .get_image import GetImage, GetImageHandler
from .json_to_zip import JsonToZip, JsonToZipHandler
from dominio.queries.createlog import CreateLog

class ImageCompiler():
    def __init__(self, list_image, zip_name: str):
        self.list_image = list_image
        self.zip_name = zip_name

    def handle(self, list_image):

        try:
            getImageHandler = GetImageHandler()
            json_list = []
            for image in list_image:
                print(image)
                json_list.append(getImageHandler.handle(GetImage(image)))
            
            # createLog = CreateLog(self.zip_name)
            # createLog.log()

            jsonToZipHandler = JsonToZipHandler()
            jsonToZipHandler.handle(JsonToZip(json_list, self.zip_name))

            print('image zipped well')
        
        except Exception as e:
            print(e)

