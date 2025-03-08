from dataclasses import dataclass, field
from datetime import datetime as dt
from uuid import UUID, uuid4

from seedwork.dominio.comandos import ComandoDominio

@dataclass
class CrearCliente(ComandoDominio):
    id_cliente: UUID = field(default_factory=uuid4)
    correo_cliente: str = None
    tipo: str = None
    servicio: str = None
    fecha_creacion: dt = field(default_factory=dt.now)

@dataclass
class EliminarCliente(ComandoDominio):
    id_cliente: UUID = field(default_factory=uuid4)
    correo_cliente: str = None
    tipo: str = None
    servicio: str = None
    fecha_creacion: dt = field(default_factory=dt.now)