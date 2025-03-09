from abc import ABC, abstractmethod


class EmailSenderPort(ABC):
    @abstractmethod
    def send_email(self):
        pass

