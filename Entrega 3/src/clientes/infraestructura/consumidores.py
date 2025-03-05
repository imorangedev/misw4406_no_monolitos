import pulsar
from pulsar.schema import AvroSchema

from aplicacion.handlers import HandlerClientes
from infraestructura.despachadores import Despachador
from infraestructura.schema.comandos import SolicitarRegistroClienteSchema, SolicitarConsultaClienteSchema
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
            topicos['topico_clientes_solicitudes_consulta'],
            subscription_name='clientes-consultas',
            consumer_type=pulsar.ConsumerType.Shared,
            schema=AvroSchema(SolicitarConsultaClienteSchema)
        )
    
    def procesar_mensaje(self, msg):
        data = msg.__dict__
        tipo = data['tipo']
        servicio = data['servicio']
        if tipo == 'Comando' and servicio == 'crear_cliente':
            HandlerClientes().handle_solicitud_creacion(data)
        elif servicio == 'Descargar':
            HandlerClientes().handle_consulta_cliente(data)

    def listen(self):
        while True:
            try:
                msg = self.consumidor_comandos.receive(timeout_millis=2000)
                if msg:
                    body = AvroSchema(SolicitarRegistroClienteSchema).decode(msg.data())
                    self.procesar_mensaje(body)
                    self.consumidor_comandos.acknowledge(msg)
            except pulsar._pulsar.Timeout:
                pass
            
            # try:
            #     msg = self.consumidor_consultas.receive(timeout_millis=2000)
            #     if msg:
            #         body = AvroSchema(OperacionesClienteSchema).decode(msg.data())
            #         self.procesar_mensaje(body)
            #         self.consumidor_consultas.acknowledge(msg)
            # except pulsar._pulsar.Timeout:
            #     pass

            try:
                msg = self.consumidor_consultas.receive(timeout_millis=2000)
                if msg:
                    body = AvroSchema(SolicitarConsultaClienteSchema).decode(msg.data())
                    self.procesar_mensaje(body)
                    self.consumidor_consultas.acknowledge(msg)
            except pulsar._pulsar.Timeout:
                pass
    
    def close(self):
        self.cliente.close()