import pulsar
import requests
from pulsar.schema import AvroSchema
from dotenv import load_dotenv

from schema.comandos import ConsultaClienteSchema
from utils import broker_host, listar_topicos

load_dotenv('.env')

class ConsumidorCliente:
    def __init__(self):
        self.cliente = pulsar.Client(broker_host())        
        topicos = listar_topicos()

        self.consumidor_consultas = self.cliente.subscribe(
            topicos['topico_clientes_consultas'],
            subscription_name='clientes-consultas',
            consumer_type=pulsar.ConsumerType.Shared,
            schema=AvroSchema(ConsultaClienteSchema)
        )
    
    def procesar_mensaje(self, msg):
        data = msg.__dict__
        tipo = data['tipo']
        estado = data['estado']
        if estado == 'ACTIVO':
            if tipo == 'Comando':
                body = {
                        "id_cliente": data['id'],
                        "tipo": "Comando",
                        "servicio": data['servicio'],
                        "data": data['data']
                        }
                r = requests.post(url='http://localhost:3000/servicios/webhooks/solicitudDescarga', json=body)
                print(r.status_code)
            elif tipo == 'Consulta':
                body = {
                        "id_cliente": data['id'],
                        "correo_cliente": data['email'],
                        "tipo": "Consulta",
                        "servicio": data['servicio'],
                        "data": data['data']
                        }
                r = requests.post(url='http://localhost:3000/servicios/webhooks/consultaDescarga', json=body)
                print(r.status_code)

    def listen(self):
        while True:           
            msg = self.consumidor_consultas.receive()
            if msg:
                body = AvroSchema(ConsultaClienteSchema).decode(msg.data())
                self.procesar_mensaje(body)
                self.consumidor_consultas.acknowledge(msg)
    
    def close(self):
        self.cliente.close()

if __name__ == '__main__':
    consumidor = ConsumidorCliente()
    try:
        consumidor.listen()
    except KeyboardInterrupt:
        consumidor.close()
