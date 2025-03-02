import time
import uuid
from pulsar.schema import String, Long, Record  

class SolicitarDescargaSchema(Record):
    id_solicitud = String(default=str(uuid.uuid4()))    
    tipo = String()
    servicio = String()    
    fecha_creacion = Long(default=int(time.time()*1000))
    id_cliente = String()
    imagenes = String()

    def __init__(self, *args, id_solicitud=None, fecha_creacion=None, **kwargs):
        super().__init__(*args, id_solicitud=id_solicitud, fecha_creacion=fecha_creacion, **kwargs)

class SolicitarConsultaCompilacionSchema(Record):
    id_solicitud = String(default=str(uuid.uuid4()))    
    tipo = String()
    servicio = String()    
    fecha_creacion = Long(default=int(time.time()*1000))
    id_cliente = String()
    correo_cliente = String()
    id_consulta = String()

    def __init__(self, *args, id_solicitud=None, fecha_creacion=None, **kwargs):
        super().__init__(*args, id_solicitud=id_solicitud, fecha_creacion=fecha_creacion, **kwargs)

class SolicitarRegistroClienteSchema(Record):
    id_solicitud = String(default=str(uuid.uuid4()))    
    tipo = String()
    servicio = String()    
    fecha_creacion = Long(default=int(time.time()*1000))
    correo_cliente = String()

    def __init__(self, *args, id_solicitud=None, fecha_creacion=None, **kwargs):
        super().__init__(*args, id_solicitud=id_solicitud, fecha_creacion=fecha_creacion, **kwargs)