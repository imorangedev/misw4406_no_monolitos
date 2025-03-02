import pulsar
from pulsar.schema import AvroSchema

from seedwork.infraestructura.utils import broker_host


class Despachador:
    def publicar_comando(self, comando, topico, schema):
        try:
            cliente = pulsar.Client(broker_host())
            publicador = cliente.create_producer(
                topico,
                schema=AvroSchema(schema),
                properties={"schema.auto.update": "true"},
            )
            publicador.send(comando)
            return {
                "response": {"msg": f"Se ha generado el siguiente comando: {comando}"},
                "status_code": 200,
            }
        except Exception as e:
            return {
                "response": {"msg": f"Ha ocurrido un error durante la solicitud: {e}"},
                "status_code": 500,
            }

    def publicar_consulta(self, consulta, topico, schema):
        try:
            cliente = pulsar.Client(broker_host())
            publicador = cliente.create_producer(
                topico,
                schema=AvroSchema(schema),
                properties={"schema.auto.update": "true"},
            )
            publicador.send(consulta)
            return {
                "response": {
                    "msg": f"Se ha generado una nueva solicitud de consulta: {consulta}"
                },
                "status_code": 200,
            }
        except Exception as e:
            return {
                "response": {"msg": f"Ha ocurrido un error durante la solicitud: {e}"},
                "status_code": 500,
            }
