import json
from seedwork.infraestructura.utils import listar_topicos
from dominio.comandos import NotificarDescarga
from infraestructura.repositorios import NotificacionRepositorioSQL
from dominio.entidades import Notificacion
from dominio.objetos_valor import EstadoNotificacion


class HandlerWorker:
    def __init__(self):
        self.topicos = listar_topicos()
        self.repositorio = NotificacionRepositorioSQL()

    def handle_mensaje_entrada(self, datos: dict):
        # Crear evento de notificación
        evento = NotificarDescarga(
            id_evento=datos.get("id_evento"),
            id_solicitud=datos.get("id_solicitud"),
            id_cliente=datos.get("id_cliente"),
            tipo=datos.get("tipo"),
            servicio=datos.get("servicio"),
            imagenes=datos.get("imagenes"),
            estado=datos.get("estado", "INICIADO"),
            fecha_creacion=datos.get("fecha_creacion"),
        )

        # Crear entidad de notificación
        notificacion = Notificacion(
            id_evento=evento.id_evento,
            id_solicitud=evento.id_solicitud,
            id_cliente=evento.id_cliente,
            tipo=evento.tipo,
            servicio=evento.servicio,
            imagenes=evento.imagenes,
            estado=EstadoNotificacion(evento.estado),
            fecha_creacion=evento.fecha_creacion,
        )

        # Guardar en repositorio
        self.repositorio.agregar(notificacion)

        return True
