import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import asyncio

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

    async def handle_mensaje_entrada(self, datos):
        # Determinar si datos es un objeto schema o un diccionario
        if hasattr(datos, "__dict__"):
            # Es un objeto schema
            id_evento = getattr(datos, "id_evento", None)
            id_solicitud = getattr(datos, "id_solicitud", None)
            id_cliente = getattr(datos, "id_cliente", None)
            tipo = getattr(datos, "tipo", None)
            servicio = getattr(datos, "servicio", None)
            imagenes = getattr(datos, "imagenes", None)
            estado = getattr(datos, "estado", "INICIADO")
            fecha_creacion = getattr(datos, "fecha_creacion", None)
        else:
            # Es un diccionario
            id_evento = datos.get("id_evento")
            id_solicitud = datos.get("id_solicitud")
            id_cliente = datos.get("id_cliente")
            tipo = datos.get("tipo")
            servicio = datos.get("servicio")
            imagenes = datos.get("imagenes")
            estado = datos.get("estado", "INICIADO")
            fecha_creacion = datos.get("fecha_creacion")

        # Convertir timestamp de milisegundos a datetime si es necesario
        if fecha_creacion and isinstance(fecha_creacion, (int, float)):
            # Convertir de milisegundos a segundos y luego a datetime
            fecha_creacion = datetime.fromtimestamp(fecha_creacion / 1000)
        elif not fecha_creacion:
            fecha_creacion = datetime.now()

        # Crear evento de notificación
        evento = NotificarDescarga(
            id_evento=id_evento,
            id_solicitud=id_solicitud,
            id_cliente=id_cliente,
            tipo=tipo,
            servicio=servicio,
            imagenes=imagenes,
            estado=estado,
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

        # Usar un bucle de eventos para manejar operaciones de IO
        await asyncio.get_event_loop().run_in_executor(
            None, lambda: self.repositorio.agregar(notificacion)
        )

        return True
