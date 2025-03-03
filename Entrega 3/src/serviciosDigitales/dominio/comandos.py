from dataclasses import dataclass, field
from datetime import datetime as dt
from uuid import UUID, uuid4

from seedwork.dominio.comandos import ComandoDominio

@dataclass
class SolicitarDescarga(ComandoDominio):
    id_solicitud: UUID = field(default_factory=uuid4)
    id_cliente: UUID = None
    tipo: str = None
    servicio: str = None
    imagenes: list = None
    fecha_creacion: dt = field(default_factory=dt.now)

@dataclass
class SolicitarConsulta(ComandoDominio):
    id_solicitud: UUID = field(default_factory=uuid4)
    id_cliente: UUID = None
    correo_cliente: str = None
    tipo: str = None
    servicio: str = None
    id_consulta: UUID = None
    fecha_creacion: dt = field(default_factory=dt.now)

@dataclass
class SolicitarCreacionCliente(ComandoDominio):
    id_solicitud: UUID = field(default_factory=uuid4)
    correo_cliente: str = None
    tipo: str = None
    servicio: str = None
    fecha_creacion: dt = field(default_factory=dt.now)