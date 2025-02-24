from dataclasses import dataclass, field
from datetime import datetime as dt
from uuid import UUID, uuid4

from seedwork.dominio.comandos import ComandoDominio

@dataclass
class EjecutarCompilacion(ComandoDominio):
    id_solicitud: UUID = field(default_factory=uuid4)
    id_cliente: UUID = None
    tipo: str = None
    servicio: str = None
    imagenes: list = None
    fecha_creacion: dt = field(default_factory=dt.now)

