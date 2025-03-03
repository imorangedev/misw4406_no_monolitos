import pulsar
from pulsar.schema import AvroSchema
from seedwork.infraestructura.utils import broker_host
from infraestructura.schema.comandos import EjecutarCompilacionSchema
from infraestructura.schema.eventos import CompilacionIniciadaSchema


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
            print(f"Comando publicado exitosamente en {topico}: {comando}")
            return {
                "response": {"msg": f"Se ha generado el siguiente comando: {comando}"},
                "status_code": 200,
            }
        except Exception as e:
            print(f"Error publicando comando: {e}")
            return {
                "response": {"msg": f"Ha ocurrido un error durante la solicitud: {e}"},
                "status_code": 500,
            }

    def publicar_evento(self, evento, topico, schema):
        try:
            cliente = pulsar.Client(broker_host())
            publicador = cliente.create_producer(
                topico,
                schema=AvroSchema(schema),
                properties={"schema.auto.update": "true"},
            )
            publicador.send(evento)
            print(f"Evento publicado exitosamente en {topico}: {evento}")
            return {
                "response": {"msg": f"Se ha generado el siguiente evento: {evento}"},
                "status_code": 200,
            }
        except Exception as e:
            print(f"Error publicando evento: {e}")
            return {
                "response": {"msg": f"Ha ocurrido un error durante la solicitud: {e}"},
                "status_code": 500,
            }
