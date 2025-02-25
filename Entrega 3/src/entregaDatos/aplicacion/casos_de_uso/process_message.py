from aplicacion.comando.handler import CommandHandler
from dominio.models import CommandMessage, message_factory
from seedwork.logger_config import get_logger


class useCaseProcessMessage:
    def __init__(self, command_handler: CommandHandler):
        self.command_handler = command_handler
        self.logger = get_logger("PROCESS_MESSAGE")

    def execute(self, message):
        try:
            message_obj = message_factory(message)

            if message_obj is None:
                self.logger.error(
                    "No se pudo procesar el mensaje, se descarta.")
                return

            message_type = message_obj.to_dict()['tipo']

            self.logger.info(
                f"Mensaje recibido | Tipo: {message_type} | Payload: {message_obj}")

            if isinstance(message_obj, CommandMessage):
                self.command_handler.handler(message_obj)

        except Exception as error:
            self.logger.error(
                f"Error procesando mensaje: {error}", exc_info=True)
            raise
