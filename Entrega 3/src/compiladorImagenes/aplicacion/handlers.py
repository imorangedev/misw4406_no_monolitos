import ast
from uuid import uuid4
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# from infraestructura.despachadores import Despachador
from seedwork.infraestructura.utils import listar_topicos
from dominio.comandos.image_compiler import ImageCompiler
from dominio.entidades import Logs
from infraestructura.model import db
from infraestructura.repositorios import LogsRepositorioSQL


class HandlerWorker:
    def __init__(self, environment: str, engine):
        self.environment = environment
        self.zip_name = str(uuid4())
        self.id_register = str(uuid4())
        self.engine = engine
        db.metadata.create_all(self.engine)
        session = sessionmaker(bind=self.engine)()
        self.topicos = listar_topicos(self.environment)
        self.repositorio = LogsRepositorioSQL(session)


    def handle_mensaje_entrada(self, cuerpo: dict):

        if cuerpo["imagenes"]:

            msg_received = cuerpo["imagenes"]
            transformed_message = ast.literal_eval(msg_received)

            comando = ImageCompiler(
                list_image=transformed_message,
                zip_name=self.zip_name
            )
            comando = comando.handle(transformed_message)

            try:
                createLog = Logs(id=self.id_register,
                                id_cliente=cuerpo["id_cliente"],
                                id_solicitud=cuerpo["id_solicitud"],
                                id_zip_file=self.zip_name)
                self.repositorio.agregar(createLog)
                print('Log guardado')
            except Exception as e:
                print(f"Error al guardar el log: {e}")
        
        else: 
            print('no image to compile')
            pass
