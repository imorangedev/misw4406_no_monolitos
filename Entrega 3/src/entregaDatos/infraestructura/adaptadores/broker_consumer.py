import pulsar
from pulsar.schema import AvroSchema
from config import Config

from dominio.schema import CommandMessage, QueryMessage
from aplicacion.casos_de_uso.process_message import useCaseProcessMessage
from config import Config
from dominio.puertos.message_consumer import MessageConsumerPort
from seedwork.logger_config import get_logger

class BrokerConsumer(MessageConsumerPort):
    def __init__(self, use_case_process_message: useCaseProcessMessage):
        self.client = pulsar.Client(Config.BROKER_HOST)
        self.use_case_process_message=use_case_process_message
        self.logger = get_logger("BROKER_CONSUMER")

        self.command_consumer = self.client.subscribe(
            Config.BROKER_COMMAND_TOPIC,
            subscription_name=Config.BROKER_COMMAND_SUBCRIPTION,
            consumer_type=pulsar.ConsumerType.Shared,
            schema=AvroSchema(CommandMessage)
        )

        self.query_consumer = self.client.subscribe(
            Config.BROKER_QUERY_TOPIC,
            subscription_name=Config.BROKER_QUERY_SUBCRIPTION,
            consumer_type=pulsar.ConsumerType.Shared,
            schema=AvroSchema(QueryMessage)
        )
    
    def _process_messages(self, msg):
        self.use_case_process_message.execute(msg)

    def consume_messages(self):
        while True:
            try:
                msg = self.command_consumer.receive(timeout_millis=3000)
                if msg:
                    body = AvroSchema(CommandMessage).decode(msg.data())
                    self._process_messages(body)
                    """ self.command_consumer.acknowledge(msg) """
            except pulsar._pulsar.Timeout:
                pass
            
            try:
                msg = self.query_consumer.receive(timeout_millis=3000)
                if msg:
                    body = AvroSchema(QueryMessage).decode(msg.data())
                    self._process_messages(body)
                    """ self.query_consumer.acknowledge(msg) """
            except pulsar._pulsar.Timeout:
                pass
    
    def close(self):
        self.client.close()