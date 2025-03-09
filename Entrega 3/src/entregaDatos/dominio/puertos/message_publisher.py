from abc import ABC, abstractmethod

class MessagePublisherPort(ABC):
    @abstractmethod
    def publish(self) -> None:
        pass
