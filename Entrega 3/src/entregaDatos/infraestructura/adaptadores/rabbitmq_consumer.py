import json
import time

import pika
from aplicacion.casos_de_uso.process_message import useCaseProcessMessage
from config import Config
from dominio.puertos.message_consumer import MessageConsumerPort
from seedwork.logger_config import get_logger


class RabbitMQConsumer(MessageConsumerPort):
    def __init__(self, queue_name: str, use_case_process_message: useCaseProcessMessage):
        self.queue_name = queue_name
        self.use_case_process_message = use_case_process_message
        self.logger = get_logger("RABBITMQ_CONSUMER")

    def _create_rabbitmq_channel(self):
        try:
            parameters = pika.URLParameters(Config.BROKER_HOST)
            connection = pika.BlockingConnection(parameters)
            channel = connection.channel()
            channel.queue_declare(queue=self.queue_name, durable=False)
            return channel
        except Exception as e:
            self.logger.error(
                f"Error al conectar con RabbitMQ: {e}", exc_info=True)
            raise

    def _callback(self, ch, method, properties, body):
        try:
            message_str = body.decode("utf-8")
            message = json.loads(message_str)
            self.use_case_process_message.execute(message)
            ch.basic_ack(delivery_tag=method.delivery_tag)

        except json.JSONDecodeError:
            self.logger.error(
                f"Mensaje JSON inválido, no se pudo decodificar: {body}")
            ch.basic_ack(delivery_tag=method.delivery_tag)

        except Exception as e:
            self.logger.error(
                f"Error procesando mensaje: {e} | Datos recibidos: {body}", exc_info=True)
            ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)

    def consume_messages(self):
        while True:
            try:
                channel = self._create_rabbitmq_channel()
                channel.basic_consume(
                    queue=self.queue_name,
                    on_message_callback=self._callback,
                    auto_ack=False
                )
                self.logger.info(
                    f"Worker en ejecución | Escuchando mensajes en la cola [{self.queue_name}]")
                channel.start_consuming()

            except Exception as e:
                self.logger.error(
                    f"Error en worker: {e} | Reintentando en 5s...", exc_info=True)
                time.sleep(5)
