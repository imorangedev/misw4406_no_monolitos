from config import Config
from dominio.puertos.email_sender import EmailSenderPort
from mailersend import emails
from seedwork.email_template import email_subject, email_template
from seedwork.logger_config import get_logger


class EmailSender(EmailSenderPort):
    def __init__(self):
        self.logger = get_logger("EMAIL_SENDER")

    def send_email(self, recipient_email: str) -> None:
        try:
            SENDGRID_FROM_EMAIL = Config.SENDGRID_FROM_EMAIL
            SENDGRID_API_KEY = Config.SENDGRID_API_KEY

            mailer = emails.NewEmail(
                ":mlsn.a0097dd57003488dad4efeaff176bace4350a5a3c35f3b40c17a1d36408a291e")

            mail_body = {}

            mail_from = {
                "name": "Your Name",
                "email": "trial-neqvygmq52540p7w.mlsender.net",
            }

            recipients = [
                {
                    "name": "Your Client",
                    "email": recipient_email,
                }
            ]

            reply_to = {
                "name": "Name",
                "email": "trial-neqvygmq52540p7w.mlsender.net",
            }

            mailer.set_mail_from(mail_from, mail_body)
            mailer.set_mail_to(recipients, mail_body)
            mailer.set_subject(email_subject, mail_body)
            mailer.set_html_content(email_template, mail_body)
            mailer.set_reply_to(reply_to, mail_body)

            print(mailer.send(mail_body))

            """ if (response.status_code == 202):
                    self.logger.info(
                        f"Email enviado a {recipient_email} correctamente.")
                else:
                    raise Exception(
                        f"No se puedo enviar el email: {recipient_email} | Status code: {response.status_code}."
                    )
 """
        except Exception as e:
            self.logger.error(
                f"Error enviando email: {e}", exc_info=True)
            raise
