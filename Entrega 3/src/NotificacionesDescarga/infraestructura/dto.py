from sqlalchemy import Column, String, UUID, Enum, DateTime
from sqlalchemy.ext.declarative import declarative_base
from dominio.objetos_valor import EstadoNotificacion

Base = declarative_base()


class NotificacionDB(Base):
    __tablename__ = "notificaciones"

    id_evento = Column(UUID, nullable=False, primary_key=True)
    id_solicitud = Column(UUID, nullable=False)
    id_cliente = Column(UUID, nullable=False)
    servicio = Column(String, nullable=False)
    imagenes = Column(String, nullable=False)
    estado = Column(Enum(EstadoNotificacion), nullable=False)
    fecha_creacion = Column(DateTime, nullable=False)
