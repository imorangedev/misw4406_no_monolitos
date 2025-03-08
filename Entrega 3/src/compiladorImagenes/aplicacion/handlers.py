import ast

from infraestructura.despachadores import Despachador
from seedwork.infraestructura.utils import listar_topicos
from dominio.comandos.image_compiler import ImageCompiler


class HandlerWorker:
    def __init__(self):
        # self.despachador = Despachador()
        self.topicos = listar_topicos()

    def handle_mensaje_entrada(self, cuerpo: dict):

        if cuerpo["imagenes"]:

            msg_received = cuerpo["imagenes"]
            transformed_message = ast.literal_eval(msg_received)

            comando = ImageCompiler(
                list_image=transformed_message
            )
            comando = comando.handle(transformed_message)
        
        else: 
            print('no image to compile')
            pass
