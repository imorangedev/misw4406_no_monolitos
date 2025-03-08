import pulsar
import aiopulsar
import logging
from pulsar.schema import AvroSchema
from seedwork.infraestructura.utils import broker_host
from infraestructura.schema.comandos import EjecutarCompilacionSchema
from infraestructura.schema.eventos import CompilacionIniciadaSchema


class Despachador:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    async def publicar_comando(self, comando, topico, schema):
        try:
            async with aiopulsar.connect(broker_host()) as cliente:
                async with cliente.create_producer(
                    topico,
                    schema=AvroSchema(schema),
                    properties={"schema.auto.update": "true"},
                ) as publicador:
                    await publicador.send(comando)
                    self.logger.info(
                        f"Comando publicado exitosamente en {topico}: {comando}"
                    )
                    return {
                        "response": {
                            "msg": f"Se ha generado el siguiente comando: {comando}"
                        },
                        "status_code": 200,
                    }
        except Exception as e:
            self.logger.error(f"Error publicando comando: {e}")
            return {
                "response": {"msg": f"Ha ocurrido un error durante la solicitud: {e}"},
                "status_code": 500,
            }

    async def publicar_evento(self, evento, topico, schema):
        try:
            async with aiopulsar.connect(broker_host()) as cliente:
                async with cliente.create_producer(
                    topico,
                    schema=AvroSchema(schema),
                    properties={"schema.auto.update": "true"},
                ) as publicador:
                    await publicador.send(evento)
                    self.logger.info(
                        f"Evento publicado exitosamente en {topico}: {evento}"
                    )
                    return {
                        "response": {
                            "msg": f"Se ha generado el siguiente evento: {evento}"
                        },
                        "status_code": 200,
                    }
        except Exception as e:
            self.logger.error(f"Error publicando evento: {e}")
            return {
                "response": {"msg": f"Ha ocurrido un error durante la solicitud: {e}"},
                "status_code": 500,
            }
