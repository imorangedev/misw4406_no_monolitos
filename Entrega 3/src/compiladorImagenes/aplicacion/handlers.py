from infraestructura.despachadores import Despachador
from seedwork.infraestructura.utils import listar_topicos
from dominio.comandos.image_compiler import ImageCompiler


class HandlerWorker:
    def __init__(self):
        self.despachador = Despachador()
        self.topicos = listar_topicos()

    def handle_mensaje_entrada(self, cuerpo: dict):
        pass
        comando = ImageCompiler(
            list_image=cuerpo["ids_imagenes"],
        )
        comando = comando.handle(cuerpo["ids_imagenes"])
        # # Publicar evento en tópico de notificaciones
        # self.despachador.publicar_comando(
        #     comando, self.topicos["topico_salida_1"], "comando"
        # )

        # # Publicar comando en tópico de procesamiento
        # self.despachador.publicar_evento(
        #     comando, self.topicos["topico_salida_2"], "evento"
        # )

        # return True