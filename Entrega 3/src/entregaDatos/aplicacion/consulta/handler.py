from dominio.schema import QueryMessage
from dominio.puertos.email_sender import EmailSenderPort
from seedwork.logger_config import get_logger


class QueryHandler:
    def __init__(self, email_sender: EmailSenderPort):
        self.email_sender = email_sender
        self.logger = get_logger("QUERY_HANDLER")

    def handler(self, message: QueryMessage) -> None:
        recipient_email = message.correo_cliente

        self.email_sender.send_email(recipient_email)

        self.logger.info(
            f"Consulta terminada | id_solicitud: {message.id_solicitud}"
        )
