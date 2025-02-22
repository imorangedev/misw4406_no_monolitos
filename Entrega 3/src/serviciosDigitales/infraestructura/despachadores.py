import pika
import json

from seedwork.infraestructura.utils import broker_host, listar_topicos

class Despachador:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.URLParameters(broker_host()))
        self.channel = self.connection.channel()

        topicos = listar_topicos()
        for key in topicos:
            self.channel.queue_declare(topicos[key])

    def publicar_comando(self, comando, topico):
        try:
            self.channel.basic_publish(
                exchange="", routing_key=topico, body=json.dumps(comando)
            )
            return {'response': {'msg': f'Se ha generado el siguiente comando: {comando}'}, 'status_code': 200}
        except:
            return {'response': {'msg': f'Ha ocurrido un error durante la solicitud: {comando}'}, 'status_code': 500}