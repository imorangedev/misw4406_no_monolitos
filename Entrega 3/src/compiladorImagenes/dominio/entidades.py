from dataclasses import dataclass, field
from datetime import datetime as dt
from uuid import UUID, uuid4

from seedwork.dominio.entidades import Entidad

@dataclass
class Logs(Entidad):
    id: str = None
    id_cliente: str = None
    id_solicitud: str = None
    id_zip_file: str = None
    # tipo: str = None
    # servicio: str = None
    # imagenes: list = None
    # estado: str = None
    # fecha_creacion: dt = field(default_factory=dt.now)