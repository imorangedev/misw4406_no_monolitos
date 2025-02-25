import json

import pika
from config import Config
from dominio.models import BaseMessage
from dominio.puertos.message_publisher import MessagePublisherPort
from seedwork.logger_config import get_logger


class RabbitMQPublisher(MessagePublisherPort):
    def __init__(self):
        self.channel = None
        self.logger = get_logger("RABBITMQ_PUBLISHER")

    def _get_channel(self):
        if self.channel is None or self.channel.is_closed:
            try:
                parameters = pika.URLParameters(Config.BROKER_HOST)
                connection = pika.BlockingConnection(parameters)
                self.channel = connection.channel()
            except Exception as e:
                self.logger.error(
                    f"Error al conectar con RabbitMQ: {e}", exc_info=True)
                raise
        return self.channel

    def publish(self, target_queue: str, message: BaseMessage) -> None:
        try:
            channel = self._get_channel()
            channel.queue_declare(queue=target_queue, durable=True)

            channel.basic_publish(
                exchange="",
                routing_key=target_queue,
                body=json.dumps(message.to_dict()),
                properties=pika.BasicProperties(
                    delivery_mode=2
                )
            )

        except Exception as e:
            self.logger.error(
                f"Error publicando mensaje en [{target_queue}]: {e}", exc_info=True)
            raise
