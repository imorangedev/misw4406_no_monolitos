import time
import uuid
from pulsar.schema import String, Record, Long 

class CommandMessage(Record):
    id_solicitud = String(default=str(uuid.uuid4()))
    fecha_creacion = Long(default=int(time.time()*1000))
    tipo = String()
    servicio = String()
    id_cliente = String()
    data = String()
    def __init__(self, *args, id_solicitud=None, fecha_creacion=None, **kwargs):
        super().__init__(*args, id_solicitud=id_solicitud, fecha_creacion=fecha_creacion, **kwargs)

class CommandOutputMessage(Record):
    id_solicitud = String(default=str(uuid.uuid4()))
    tipo = String()
    servicio = String()
    fecha_creacion = Long(default=int(time.time()*1000))
    id_cliente = String()
    imagenes = String()
    def __init__(self, *args, id_solicitud=None, fecha_creacion=None, **kwargs):
        super().__init__(*args, id_solicitud=id_solicitud, fecha_creacion=fecha_creacion, **kwargs)

class QueryMessage(Record):
    id_solicitud = String(default=str(uuid.uuid4()))
    fecha_creacion = Long(default=int(time.time()*1000))
    tipo = String()
    servicio = String()
    id_cliente = String()
    correo_cliente = String()
    data = String()
    def __init__(self,id_solicitud=None, fecha_creacion=None, *args, **kwargs):
        super().__init__(*args, id_solicitud=id_solicitud, fecha_creacion=fecha_creacion, **kwargs)