from dataclasses import dataclass, field
import uuid
from datetime import datetime


@dataclass
class EventoDominio:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    fecha_evento: datetime = field(default_factory=datetime.now)


@dataclass
class NotificacionEnviada(EventoDominio):
    id_notificacion: uuid.UUID = None
    id_compilacion: uuid.UUID = None
    id_datos: uuid.UUID = None
    detalles: dict = field(default_factory=dict)
    tipo_evento: str = "NotificacionEnviada"

    def to_dict(self):
        return {
            "id": str(self.id),
            "fecha_evento": self.fecha_evento.isoformat(),
            "id_notificacion": (
                str(self.id_notificacion) if self.id_notificacion else None
            ),
            "id_compilacion": str(self.id_compilacion) if self.id_compilacion else None,
            "id_datos": str(self.id_datos) if self.id_datos else None,
            "detalles": self.detalles,
            "tipo_evento": self.tipo_evento,
        }


@dataclass
class EnvioNotificacionFallido(EventoDominio):
    id_notificacion: uuid.UUID = None
    id_compilacion: uuid.UUID = None
    id_datos: uuid.UUID = None
    error: str = None
    tipo_evento: str = "EnvioNotificacionFallido"

    def to_dict(self):
        return {
            "id": str(self.id),
            "fecha_evento": self.fecha_evento.isoformat(),
            "id_notificacion": (
                str(self.id_notificacion) if self.id_notificacion else None
            ),
            "id_compilacion": str(self.id_compilacion) if self.id_compilacion else None,
            "id_datos": str(self.id_datos) if self.id_datos else None,
            "error": self.error,
            "tipo_evento": self.tipo_evento,
        }
