import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from config import Config
from seedwork.infraestructura.utils import listar_topicos
from dominio.comandos import NotificarDescarga
from infraestructura.dto import Base
from infraestructura.repositorios import NotificacionRepositorioSQL
from dominio.entidades import Notificacion
from dominio.objetos_valor import EstadoNotificacion


class HandlerWorker:
    def __init__(self):
        database_URI = Config().SQLALCHEMY_DATABASE_URI
        self.engine = create_engine(database_URI)
        Base.metadata.create_all(self.engine)
        session = sessionmaker(bind=self.engine)()
        self.topicos = listar_topicos()
        self.repositorio = NotificacionRepositorioSQL(session)

    def handle_mensaje_entrada(self, datos: dict):
        # Convertir timestamp de milisegundos a datetime si es necesario
        fecha_creacion = datos.get("fecha_creacion")
        if fecha_creacion and isinstance(fecha_creacion, (int, float)):
            # Convertir de milisegundos a segundos y luego a datetime
            fecha_creacion = datetime.fromtimestamp(fecha_creacion / 1000)
        else:
            fecha_creacion = datetime.now()

        # Crear evento de notificación
        evento = NotificarDescarga(
            id_evento=datos.get("id_evento"),
            id_solicitud=datos.get("id_solicitud"),
            id_cliente=datos.get("id_cliente"),
            tipo=datos.get("tipo"),
            servicio=datos.get("servicio"),
            imagenes=datos.get("imagenes"),
            estado=datos.get("estado", "INICIADO"),
            fecha_creacion=fecha_creacion,
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
