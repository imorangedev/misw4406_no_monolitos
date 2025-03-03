import time
import uuid
from pulsar.schema import String, Long, Record  

class SolicitarRegistroClienteSchema(Record):
    tipo = String()
    servicio = String()    
    nombre = String()
    email = String()
    pais = String()
    estado = String()
    suscripcion = String()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class OperacionesClienteSchema(Record):
    id_solicitud = String(default=str(uuid.uuid4()))    
    tipo = String()
    servicio = String()    
    fecha_creacion = Long(default=int(time.time()*1000))
    id_cliente = String()

    def __init__(self, *args, id_solicitud=None, fecha_creacion=None, **kwargs):
        super().__init__(*args, id_solicitud=id_solicitud, fecha_creacion=fecha_creacion, **kwargs)