from aplicacion.casos_de_uso.process_message import useCaseProcessMessage
from aplicacion.comando.handler import CommandHandler
from config import Config
from dominio.puertos.message_consumer import MessageConsumerPort
from dominio.puertos.message_publisher import MessagePublisherPort
from infraestructura.adaptadores.rabbitmq_consumer import RabbitMQConsumer
from infraestructura.adaptadores.rabbitmq_publisher import RabbitMQPublisher

if __name__ == "__main__":

    message_publisher: MessagePublisherPort = RabbitMQPublisher()
    command_handler = CommandHandler(message_publisher)

    use_case_process_message = useCaseProcessMessage(command_handler)

    RABBITMQ_INPUT_QUEUE = Config.RABBITMQ_INPUT_QUEUE
    consumer: MessageConsumerPort = RabbitMQConsumer(
        RABBITMQ_INPUT_QUEUE, use_case_process_message)
    consumer.consume_messages()
