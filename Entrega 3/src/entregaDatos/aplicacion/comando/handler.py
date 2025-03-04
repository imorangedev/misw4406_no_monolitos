from config import Config
from dominio.schema import CommandMessage
from dominio.puertos.message_publisher import MessagePublisherPort
from seedwork.logger_config import get_logger


class CommandHandler:
    def __init__(self, message_publisher: MessagePublisherPort):
        self.message_publisher = message_publisher
        self.BROKER_COMMAND_OUTPUT_TOPIC = Config.BROKER_COMMAND_OUTPUT_TOPIC
        self.logger = get_logger("COMMAND_HANDLER")

    def handler(self, message: CommandMessage) -> None:
        message_id = message.id_solicitud
        self.message_publisher.publish(message)
        self.logger.info(
            f"Comando Enviado | id_solicitud: {message_id} | Destino [{self.BROKER_COMMAND_OUTPUT_TOPIC}]"
        )
