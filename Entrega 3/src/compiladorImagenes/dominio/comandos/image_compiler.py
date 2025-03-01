from uuid import uuid4

from .base_comand import Comand, ComandHandler
from .get_image import GetImage, GetImageHandler
from .json_to_zip import JsonToZip, JsonToZipHandler
from dominio.queries.createlog import CreateLog
from infraestructura.model import db, LogsImagecompiler

class ImageCompiler(Comand):
    def __init__(self, list_image: list):
        self.list_image = list_image
        self.zip_name = str(uuid4())

    def handle(self, list_image: list):
        
        try:
            getImageHandler = GetImageHandler()
            json_list = []
            for image in list_image:
                json_list.append(getImageHandler.handle(GetImage(image)))
            
            # createLog = CreateLog(self.zip_name)
            # createLog.handle()

            jsonToZipHandler = JsonToZipHandler()
            jsonToZipHandler.handle(JsonToZip(json_list, self.zip_name))

            print('image zipped well')
        
        except Exception as e:
            print(e)

