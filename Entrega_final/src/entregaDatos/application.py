import asyncio
import signal
import sys
import logging

from aplicacion.casos_de_uso.process_message import useCaseProcessMessage
from aplicacion.comando.handler import CommandHandler
from aplicacion.consulta.handler import QueryHandler
from config import Config
from dominio.puertos.email_sender import EmailSenderPort
from dominio.puertos.message_consumer import MessageConsumerPort
from dominio.puertos.message_publisher import MessagePublisherPort
from infraestructura.adaptadores.broker_consumer import BrokerConsumer
from infraestructura.adaptadores.broker_publisher import BrokerPublisher
from infraestructura.adaptadores.email_sender import EmailSender

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


async def main():
    # Configurar manejadores de señales
    def signal_handler(sig, frame):
        logger.info("Señal de interrupción recibida")
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    try:
        message_publisher: MessagePublisherPort = BrokerPublisher()
        command_handler = CommandHandler(message_publisher)

        email_sender: EmailSenderPort = EmailSender()
        query_handler = QueryHandler(email_sender)

        use_case_process_message = useCaseProcessMessage(command_handler, query_handler)

        consumer: MessageConsumerPort = BrokerConsumer(use_case_process_message)

        # Iniciar el consumo de mensajes (ahora debería ser una función asíncrona)
        await consumer.consume_messages()

    except KeyboardInterrupt:
        logger.info("Interrupción por teclado")
    except Exception as e:
        logger.error(f"Error en el servicio de entrega de datos: {e}")


if __name__ == "__main__":
    asyncio.run(main())
