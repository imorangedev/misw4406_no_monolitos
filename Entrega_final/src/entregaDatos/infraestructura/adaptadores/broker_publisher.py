import pulsar
from pulsar.schema import AvroSchema
from config import Config
from dominio.puertos.message_publisher import MessagePublisherPort
from seedwork.logger_config import get_logger
from dominio.schema import CommandMessage,CommandOutputMessage


class BrokerPublisher(MessagePublisherPort):
    def __init__(self):
        self.client = None
        self.producer = None
        self.target_topic = Config.BROKER_COMMAND_OUTPUT_TOPIC
        self.logger = get_logger("PULSAR_PUBLISHER")

    def _get_client(self):
        if self.client is None:
            try:
                self.client = pulsar.Client(Config.BROKER_HOST)
            except Exception as e:
                self.logger.error(f"Error al conectar con Pulsar: {e}", exc_info=True)
                raise
        return self.client

    def _get_producer(self, topic):
        if self.producer is None:
            try:
                client = self._get_client()
                self.producer = client.create_producer(
                    topic, schema=AvroSchema(CommandOutputMessage)
                )
            except Exception as e:
                self.logger.error(f"Error al crear productor para {topic}: {e}", exc_info=True)
                raise
        return self.producer

    def publish(self, message: CommandMessage) -> None:
        try:
            producer = self._get_producer(self.target_topic)

            output_message = CommandOutputMessage(
            id_solicitud=message.id_solicitud,
            fecha_creacion=message.fecha_creacion,
            tipo=message.tipo,
            servicio=message.servicio,
            id_cliente=message.id_cliente,
            imagenes=message.data  
            )
    
            producer.send(output_message)
        except Exception as e:
            self.logger.error(f"Error publicando mensaje en [{self.target_topic}]: {e}", exc_info=True)
            raise
