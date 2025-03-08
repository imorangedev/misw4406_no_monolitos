from mailjet_rest import Client
from config import Config
from dominio.puertos.email_sender import EmailSenderPort
from seedwork.email_template import email_template_no_notification, email_subject_no_notification
from seedwork.logger_config import get_logger


class EmailSender(EmailSenderPort):
    def __init__(self):
        self.logger = get_logger("EMAIL_SENDER")
        self.api_key=Config.EMAIL_API_KEY
        self.api_secret=Config.EMAIL_API_SECRET
        self.from_email = Config.FROM_EMAIL

    def send_email(self, recipient_email: str) -> None:
        try:
            mailjet = Client(auth=(self.api_key, self.api_secret), version='v3.1')
            data = {
                'Messages': [
                    {
                        "From": {
                            "Email": self.from_email,
                        },
                        "To": [
                            {
                                "Email": recipient_email,
                            }
                        ],
                        "Subject": email_subject_no_notification,
                        "HTMLPart": email_template_no_notification
                    }
                ]
            }
            result = mailjet.send.create(data=data)
            status_code=result.status_code
            self.logger.info(f"Send email status code: {status_code}")
        except Exception as e:
            self.logger.error(f"Error enviando email: {e}", exc_info=True)
            raise
