from uuid import uuid4

from dominio.comandos.base_comand import BaseComand
from infraestructura.model import LogsImagecompiler

class CreateLog(BaseComand):
    def __init__(self, id_zip_file: str):
        super().__init__()
        self.id_zip_file = id_zip_file

    def handle(self):
        id = str(uuid4())
        log = LogsImagecompiler(id=id, id_zip_file=self.id_zip_file)
        log.save()
        return True