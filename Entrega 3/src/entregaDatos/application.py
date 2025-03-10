from aplicacion.casos_de_uso.process_message import useCaseProcessMessage
from aplicacion.comando.handler import CommandHandler
from aplicacion.consulta.handler import QueryHandler
from config import Config
from dominio.puertos.email_sender import EmailSenderPort
from dominio.puertos.message_consumer import MessageConsumerPort
from dominio.puertos.message_publisher import MessagePublisherPort
from dominio.puertos.compilation_repository import CompilationRepositoryPort
from infraestructura.adaptadores.broker_consumer import BrokerConsumer
from infraestructura.adaptadores.broker_publisher import BrokerPublisher
from infraestructura.adaptadores.compilation_repository import CompilationRepository
from infraestructura.adaptadores.email_sender import EmailSender


if __name__ == "__main__":

    message_publisher: MessagePublisherPort = BrokerPublisher()
    command_handler = CommandHandler(message_publisher)

    compilation_repository: CompilationRepositoryPort = CompilationRepository(Config.SQLALCHEMY_DATABASE_URI)
    email_sender: EmailSenderPort = EmailSender()
    query_handler = QueryHandler(email_sender, compilation_repository)

    use_case_process_message = useCaseProcessMessage(command_handler,query_handler)
    
    consumer: MessageConsumerPort = BrokerConsumer(use_case_process_message)
    consumer.consume_messages()
