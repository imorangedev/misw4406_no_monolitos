from abc import ABC, abstractmethod
from uuid import UUID

from seedwork.dominio.entidades import Entidad

class RepositorioClientes(ABC):
    @abstractmethod
    def obtener_cliente_por_id(self, id:UUID):
        ...
    
    @abstractmethod
    def crear_cliente(self, entidad: Entidad):
        ...
    
    @abstractmethod
    def eliminar_cliente(self, entidad: Entidad):
        ...
    
class Mapeador(ABC):
    @abstractmethod
    def entidad_a_dto(self, entidad: Entidad) -> any:
        ...
    
    @abstractmethod
    def dto_a_entidad(self, dto: any) -> Entidad:
        ...