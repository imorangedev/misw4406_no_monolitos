from uuid import uuid4
from sqlalchemy import insert, cast

# from dominio.comandos.base_comand import BaseComand
from infraestructura.model import LogsImagecompiler, db

class CreateLog():
    def __init__(self, id_cliente, id_solicitud, id_zip_file):
        self.id_cliente = id_cliente
        self.id_solicitud = id_solicitud
        self.id_zip_file = id_zip_file

    def log(self):
        try:

            log = LogsImagecompiler(
                id=str(uuid4()),
                id_cliente=self.id_cliente,
                id_solicitud=self.id_solicitud,
                id_zip_file=self.id_zip_file
            )

            db.session.add(log)
            db.session.commit()
            db.session.close()

        except Exception as e:
            print(f"Error al guardar el log: {e}")