from aplicacion.comando.handler import CommandHandler
from aplicacion.consulta.handler import QueryHandler
from seedwork.logger_config import get_logger


class useCaseProcessMessage:
    def __init__(self, command_handler: CommandHandler,query_handler:QueryHandler):
        self.command_handler = command_handler
        self.query_handler = query_handler
        self.logger = get_logger("PROCESS_MESSAGE")

    def execute(self, message):
        try:
            print("\n")
            type = message.tipo
            if(type =="Comando"):
                self.command_handler.handler(message)
            elif (type == "Consulta"):
                self.query_handler.handler(message)
            return
        except Exception as error:
            self.logger.error(
                f"Error procesando mensaje: {error}", exc_info=True)
            raise