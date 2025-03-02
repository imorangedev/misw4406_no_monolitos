from infraestructura.despachadores import Despachador
from seedwork.infraestructura.utils import listar_topicos
from dominio.comandos import EjecutarCompilacion
from dominio.eventos import CompilacionIniciada


class HandlerWorker:
    def __init__(self):
        self.despachador = Despachador()
        self.topicos = listar_topicos()

    def handle_mensaje_entrada(self, cuerpo: dict):
        # Crear comando de dominio
        comando = EjecutarCompilacion(
            id_solicitud=cuerpo["id_solicitud"],
            id_cliente=cuerpo["id_cliente"],
            tipo=cuerpo["tipo"],
            servicio=cuerpo["servicio"],
            imagenes=cuerpo["imagenes"],
        )
        comando_dict = comando.to_dict()

        # Crear evento de dominio
        evento = CompilacionIniciada(
            id_solicitud=cuerpo["id_solicitud"],
            id_cliente=cuerpo["id_cliente"],
            tipo=cuerpo["tipo"],
            servicio=cuerpo["servicio"],
            imagenes=cuerpo["imagenes"],
            estado="INICIADO",
        )
        evento_dict = evento.to_dict()

        # Publicar comando en tópico de notificaciones usando schema
        self.despachador.publicar_comando(
            comando_dict, self.topicos["topico_salida_1"], "comando"
        )

        # Publicar evento en tópico de procesamiento usando schema
        self.despachador.publicar_evento(
            evento_dict, self.topicos["topico_salida_2"], "evento"
        )

        return True
