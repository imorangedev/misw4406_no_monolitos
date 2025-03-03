from abc import ABC, abstractmethod
from uuid import UUID

from seedwork.dominio.entidades import Entidad


class NotificacionRepositorio(ABC):
    @abstractmethod
    def agregar(self, notificacion: Entidad): ...

class Mapeador(ABC):
    @abstractmethod
    def entidad_a_dto(self, entidad): ...

    @abstractmethod
    def dto_a_entidad(self, dto): ...
