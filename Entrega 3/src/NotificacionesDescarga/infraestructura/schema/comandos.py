import time
import uuid
from pulsar.schema import String, Long, Record


class NotificacionDescargaSchema(Record):
    id_evento = String(default=str(uuid.uuid4()))
    id_solicitud = String()
    tipo = String()
    servicio = String()
    fecha_creacion = Long(default=int(time.time() * 1000))
    id_cliente = String()
    imagenes = String()
    estado = String()

    def __init__(self, *args, id_evento=None, fecha_creacion=None, **kwargs):
        super().__init__(
            *args, id_evento=id_evento, fecha_creacion=fecha_creacion, **kwargs
        )
