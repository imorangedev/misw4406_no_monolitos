from infraestructura.despachadores import Despachador
from seedwork.infraestructura.utils import listar_topicos
from dominio.comandos import Comando


class HandlerWorker:
    def __init__(self):
        self.despachador = Despachador()
        self.topicos = listar_topicos()

    def handle_mensaje_entrada(self, comando: dict):
        # Publicar evento en tópico de notificaciones
        self.despachador.publicar_mensaje(
            comando, self.topicos["topico_salida_1"], "evento"
        )

        # Publicar comando en tópico de procesamiento
        self.despachador.publicar_mensaje(
            comando, self.topicos["topico_salida_2"], "comando"
        )

        return True
