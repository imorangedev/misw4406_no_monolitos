from dataclasses import dataclass, field
from datetime import datetime as dt
from uuid import UUID, uuid4

from seedwork.dominio.entidades import Entidad
from dominio.objetos_valor import EstadoNotificacion


@dataclass
class Notificacion(Entidad):
    id_evento: UUID = None
    id_solicitud: UUID = None
    id_cliente: UUID = None
    tipo: str = None
    servicio: str = None
    imagenes: list = None
    estado: EstadoNotificacion = field(default_factory=EstadoNotificacion)
    fecha_creacion: dt = field(default_factory=dt.now)
