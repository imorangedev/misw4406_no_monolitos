from infraestructura.despachadores import Despachador
from seedwork.infraestructura.utils import listar_topicos
from dominio.comandos import EjecutarCompilacion


class HandlerWorker:
    def __init__(self):
        self.despachador = Despachador()
        self.topicos = listar_topicos()

    def handle_mensaje_entrada(self, cuerpo: dict):
        comando = EjecutarCompilacion(
            id_solicitud=cuerpo["id_solicitud"],
            id_cliente=cuerpo["id_cliente"],
            tipo=cuerpo["tipo"],
            servicio=cuerpo["servicio"],
            imagenes=cuerpo["imagenes"]
        )
        comando = comando.to_dict()
        # Publicar evento en tópico de notificaciones
        self.despachador.publicar_comando(
            comando, self.topicos["topico_salida_1"], "comando"
        )

        # Publicar comando en tópico de procesamiento
        self.despachador.publicar_evento(
            comando, self.topicos["topico_salida_2"], "evento"
        )

        return True
