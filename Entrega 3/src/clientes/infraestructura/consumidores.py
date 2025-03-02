import pulsar
from pulsar.schema import AvroSchema

from aplicacion.handlers import HandlerClientes
from infraestructura.despachadores import Despachador
from infraestructura.schema.comandos import SolicitarRegistroClienteSchema, OperacionesClienteSchema
from seedwork.infraestructura.utils import broker_host, listar_topicos

class ConsumidorCliente:
    def __init__(self):
        self.cliente = pulsar.Client(broker_host())
        self.despachador = Despachador()
        
        topicos = listar_topicos()

        self.consumidor_comandos = self.cliente.subscribe(
            topicos['topico_clientes_comandos'],
            subscription_name='clientes-comandos',
            consumer_type=pulsar.ConsumerType.Shared,
            schema=AvroSchema(SolicitarRegistroClienteSchema)
        )

        self.consumidor_consultas = self.cliente.subscribe(
            topicos['topico_clientes_consultas'],
            subscription_name='clientes-consultas',
            consumer_type=pulsar.ConsumerType.Shared,
            schema=AvroSchema(OperacionesClienteSchema)
        )
    
    def procesar_mensaje(self, msg):
        data = msg.__dict__
        servicio = data['servicio']
        if servicio == 'crear_cliente':
            HandlerClientes().handle_solicitud_creacion(data)
        elif servicio == 'eliminar_cliente':
            HandlerClientes().handle_consulta_cliente(data)
        elif servicio == 'consultar_cliente':
            HandlerClientes().handle_consulta_cliente(data)

    def listen(self):
        while True:
            try:
                msg = self.consumidor_comandos.receive(timeout_millis=3000)
                if msg:
                    msg = AvroSchema(SolicitarRegistroClienteSchema).decode(msg.data())
                    self.procesar_mensaje(msg)
                    self.consumidor_comandos.acknowledge(msg)
            except pulsar._pulsar.Timeout:
                pass
            
            try:
                msg = self.consumidor_consultas.receive(timeout_millis=3000)
                if msg:
                    msg = AvroSchema(OperacionesClienteSchema).decode(msg.data())
                    self.procesar_mensaje(msg)
                    self.consumidor_consultas.acknowledge(msg)
            except pulsar._pulsar.Timeout:
                pass
    
    def close(self):
        self.cliente.close()