from pulsar.schema import String, Record  

class SolicitarDescargaSchema(Record): 
    tipo = String()
    servicio = String()    
    id_cliente = String()
    imagenes = String()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class SolicitarConsultaCompilacionSchema(Record):  
    tipo = String()
    servicio = String()    
    id_cliente = String()
    correo_cliente = String()
    id_consulta = String()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

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