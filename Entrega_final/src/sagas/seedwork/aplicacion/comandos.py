from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
import uuid


class Comando(ABC):
    @abstractmethod
    def ejecutar(self): ...


@dataclass
class ComandoIntegracion(Comando):
    id: uuid.UUID = uuid.uuid4()
    fecha_comando: datetime = datetime.now()
    id_correlacion: uuid.UUID = None


def ejecutar_commando(comando):
    comando.ejecutar()
