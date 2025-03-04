from dominio.models import QueryMessage
from dominio.puertos.email_sender import EmailSenderPort
from seedwork.logger_config import get_logger


class QueryHandler:
    def __init__(self, email_sender: EmailSenderPort):
        self.email_sender = email_sender
        self.logger = get_logger("QUERY_HANDLER")

    def handler(self, message: QueryMessage) -> None:
        message_as_dict = message.to_dict()
        recipient_email = message_as_dict.get("correo_cliente", "N/A")

        self.email_sender.send_email(recipient_email)

        self.logger.info(
            f"Consulta terminada | ID: {message_as_dict.get('id_consulta', 'N/A')}"
        )
