from infraestructura.despachadores import Despachador
from seedwork.infraestructura.utils import listar_topicos
from dominio.comandos import Comando


class HandlerWorker:
    def __init__(self):
        self.despachador = Despachador()
        self.topicos = listar_topicos()

    def handle_mensaje_entrada(self, cuerpo: dict):
        comando = Comando(
            id_cliente=cuerpo["id_cliente"],
            tipo=cuerpo["tipo"],
            servicio=cuerpo["servicio"],
            imagenes=cuerpo["imagenes"]
        )
        # Publicar evento en tópico de notificaciones
        self.despachador.publicar_mensaje(
            comando, self.topicos["topico_salida_1"], "comando"
        )

        # Publicar comando en tópico de procesamiento
        self.despachador.publicar_mensaje(
            comando, self.topicos["topico_salida_2"], "evento"
        )

        return True
