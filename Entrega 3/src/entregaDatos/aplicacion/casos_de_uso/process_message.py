from seedwork.logger_config import get_logger
from dominio.models import CommandMessage
from dominio.models import message_factory
from aplicacion.comando.handler import CommandHandler

class useCaseProcessMessage:
    def __init__(self, command_handler: CommandHandler):
        self.command_handler = command_handler
        self.logger = get_logger("PROCESS_MESSAGE")

    def execute(self, message):
        try:
            message_obj = message_factory(message)

            if message_obj is None: 
                self.logger.error("No se pudo procesar el mensaje, se descarta.")
                return

            message_type=message_obj.to_dict()['tipo']
            message_id=message_obj.to_dict().get('id_solicitud', 'N/A')

            self.logger.info(f"Mensaje recibido | Tipo: {message_type} | Payload: {message_obj}")

            if isinstance(message_obj, CommandMessage):
                self.command_handler.handler(message_obj)

        except Exception as error:
            self.logger.error(f"Error procesando mensaje: {error}", exc_info=True)
            raise
