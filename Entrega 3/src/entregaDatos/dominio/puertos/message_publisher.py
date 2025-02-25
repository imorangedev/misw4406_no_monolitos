from abc import ABC, abstractmethod
from dominio.models import BaseMessage

class MessagePublisherPort(ABC):
    @abstractmethod
    def publish(self, target_queue: str, message: BaseMessage) -> None:
        pass