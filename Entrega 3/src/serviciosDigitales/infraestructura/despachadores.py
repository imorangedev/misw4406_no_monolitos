import pulsar
import json

from seedwork.infraestructura.utils import broker_host


class Despachador:
    def __init__(self):
        self.cliente = pulsar.Client(broker_host())

    def publicar_comando(self, comando, topico):
        try:
            publicador = self.cliente.create_producer(topico)
            publicador.send(
                json.dumps(comando, default=str).encode('utf-8')
            )
            return {
                "response": {"msg": f"Se ha generado el siguiente comando: {comando}"},
                "status_code": 200,
            }
        except Exception as e:
            return {
                "response": {
                    "msg": f"Ha ocurrido un error durante la solicitud: {e}"
                },
                "status_code": 500,
            }
    
    def publicar_consulta(self, consulta, topico):
        try:
            publicador = self.cliente.create_producer(topico)
            publicador.send(
                json.dumps(consulta, default=str).encode('utf-8')
            )
            return {
                "response": {"msg": f"Se ha generado una nueva solicitud de consulta: {consulta}"},
                "status_code": 200,
            }
        except Exception as e:
            return {
                "response": {
                    "msg": f"Ha ocurrido un error durante la solicitud: {e}"
                },
                "status_code": 500,
            }
