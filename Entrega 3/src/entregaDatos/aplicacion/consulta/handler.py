from dominio.schema import QueryMessage
from dominio.puertos.email_sender import EmailSenderPort
from seedwork.logger_config import get_logger
from dominio.puertos.compilation_repository import CompilationRepositoryPort

class QueryHandler:
    def __init__(self, email_sender: EmailSenderPort, compilation_repository: CompilationRepositoryPort):
        self.compilation_repository=compilation_repository
        self.email_sender = email_sender
        self.logger = get_logger("QUERY_HANDLER")

    def handler(self, message: QueryMessage) -> None:

        recipient_email = message.correo_cliente

        compilation = self.compilation_repository.find_by_property("id_solicitud", message.id_solicitud)

        compilation_validation=len(compilation)>0

        self.logger.info("No se encontraron datos de compilaciones" if compilation_validation == False else "Se encontraron datos de compilaciones")

        self.email_sender.send_email(recipient_email, compilation_validation)

        self.logger.info(
            f"Consulta terminada | id_solicitud: {message.id_solicitud}"
        )

