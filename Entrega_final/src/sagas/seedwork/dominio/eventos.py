from abc import ABC
from dataclasses import dataclass
from datetime import datetime
import uuid


@dataclass
class EventoDominio(ABC):
    id: uuid.UUID = uuid.uuid4()
    fecha_evento: datetime = datetime.now()


@dataclass
class EventoIntegracion(EventoDominio):
    id_correlacion: uuid.UUID = None
