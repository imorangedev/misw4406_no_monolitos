from dataclasses import dataclass, field
from datetime import datetime as dt
from uuid import UUID, uuid4
import uuid

from seedwork.dominio.comandos import ComandoDominio


@dataclass
class EventoDominio:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    fecha_evento: dt = field(default_factory=dt.now)


@dataclass
class CompilacionIniciada(ComandoDominio):
    id_evento: UUID = field(default_factory=uuid4)
    id_solicitud: UUID = None
    id_cliente: UUID = None
    tipo: str = None
    servicio: str = None
    imagenes: list = None
    estado: str = "INICIADO"
    fecha_creacion: dt = field(default_factory=dt.now)

    def to_dict(self):
        # Convertir los campos a sus representaciones en string
        return {
            "id_evento": str(self.id_evento),
            "id_solicitud": str(self.id_solicitud),
            "id_cliente": str(self.id_cliente),
            "tipo": self.tipo,
            "servicio": self.servicio,
            "imagenes": self.imagenes,
            "estado": self.estado,
            "fecha_creacion": self.fecha_creacion.isoformat(),
        }


@dataclass
class CompilacionPublicada(EventoDominio):
    id_compilacion: UUID = None
    id_datos: UUID = None
    detalles: dict = field(default_factory=dict)
    tipo_evento: str = "CompilacionPublicada"

    def to_dict(self):
        return {
            "id": str(self.id),
            "fecha_evento": self.fecha_evento.isoformat(),
            "id_compilacion": str(self.id_compilacion) if self.id_compilacion else None,
            "id_datos": str(self.id_datos) if self.id_datos else None,
            "detalles": self.detalles,
            "tipo_evento": self.tipo_evento,
        }


@dataclass
class PublicacionCompilacionFallida(EventoDominio):
    id_compilacion: UUID = None
    id_datos: UUID = None
    error: str = None
    tipo_evento: str = "PublicacionCompilacionFallida"

    def to_dict(self):
        return {
            "id": str(self.id),
            "fecha_evento": self.fecha_evento.isoformat(),
            "id_compilacion": str(self.id_compilacion) if self.id_compilacion else None,
            "id_datos": str(self.id_datos) if self.id_datos else None,
            "error": self.error,
            "tipo_evento": self.tipo_evento,
        }
