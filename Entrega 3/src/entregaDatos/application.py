from config import Config
from aplicacion.comando.handler import CommandHandler
from aplicacion.casos_de_uso.process_message import useCaseProcessMessage
from infraestructura.adaptadores.rabbitmq_consumer import RabbitMQConsumer
from infraestructura.adaptadores.rabbitmq_publisher import RabbitMQPublisher  
from dominio.puertos.message_publisher import MessagePublisherPort
from dominio.puertos.message_consumer import MessageConsumerPort

if __name__ == "__main__":

    message_publisher: MessagePublisherPort = RabbitMQPublisher()
    command_handler = CommandHandler(message_publisher)
    
    use_case_process_message = useCaseProcessMessage(command_handler)

    RABBITMQ_INPUT_QUEUE = Config.RABBITMQ_INPUT_QUEUE
    consumer: MessageConsumerPort = RabbitMQConsumer(RABBITMQ_INPUT_QUEUE, use_case_process_message)
    consumer.consume_messages()