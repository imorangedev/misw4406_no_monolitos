from dataclasses import dataclass, field
import uuid
from datetime import datetime


@dataclass
class EventoDominio:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    fecha_evento: datetime = field(default_factory=datetime.now)


@dataclass
class DatosEntregados(EventoDominio):
    id_datos: uuid.UUID = None
    detalles: dict = field(default_factory=dict)
    tipo_evento: str = "DatosEntregados"


@dataclass
class EntregaDatosFallida(EventoDominio):
    id_datos: uuid.UUID = None
    error: str = None
    tipo_evento: str = "EntregaDatosFallida"
