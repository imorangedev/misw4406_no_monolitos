import time
import uuid
from pulsar.schema import String, Long, Record


class NotificacionDescargaSchema(Record):
    id_evento = String()
    id_solicitud = String()
    id_cliente = String()
    servicio = String()
    fecha_creacion = Long()
    imagenes = String()
    estado = String()

    def __init__(self, *args, **kwargs):
        super().__init__(
            *args, **kwargs
        )
