from config import Config
from dominio.models import CommandMessage
from dominio.puertos.message_publisher import MessagePublisherPort
from seedwork.logger_config import get_logger


class CommandHandler:
    def __init__(self, message_publisher: MessagePublisherPort):
        self.message_publisher = message_publisher
        self.RABBITMQ_OUTPUT_QUEUE = Config.RABBITMQ_OUTPUT_QUEUE
        self.logger = get_logger("COMMAND_HANDLER")

    def handler(self, message: CommandMessage) -> None:
        message_as_dict = message.to_dict()
        message_id = message_as_dict.get("id_solicitud", "N/A")

        self.message_publisher.publish(self.RABBITMQ_OUTPUT_QUEUE, message)
        self.logger.info(
            f"Comando Enviado | ID: {message_id} | Destino [{self.RABBITMQ_OUTPUT_QUEUE}]"
        )
