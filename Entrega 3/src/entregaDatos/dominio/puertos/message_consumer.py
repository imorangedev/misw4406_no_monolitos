from abc import ABC, abstractmethod

class MessageConsumerPort(ABC):
    @abstractmethod
    def consume_messages(self):
        pass
