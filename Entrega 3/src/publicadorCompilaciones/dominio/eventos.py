from dataclasses import dataclass, field
from datetime import datetime as dt
from uuid import UUID, uuid4

from seedwork.dominio.comandos import ComandoDominio


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
