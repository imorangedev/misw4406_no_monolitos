from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from uuid import UUID

from dominio.entidades import Cliente
from dominio.repositorios import RepositorioClientes
from aplicacion.mapeadores import MapeadorCliente
from infraestructura.dto import ClienteDB

class RepositorioClientesSQLAlchemy(RepositorioClientes):
    def __init__(self, session: Session):
        self.session = session
        self.mapeador = MapeadorCliente()

    def obtener_cliente_por_id(self, id: UUID) -> Cliente:
        try:
            dto = self.session.query(ClienteDB).filter_by(id=id).first()
            return self.mapeador.dto_a_entidad(dto)
        except NoResultFound:
            return {'response': {'msg:' 'No se ha encontrado al cliente solicitado'}, 'status_code': 400}
    
    def crear_cliente(self, entidad: Cliente) -> None:
        dto = self.mapeador.entidad_a_dto(entidad)
        self.session.add(dto)
        self.session.commit()
    
    def eliminar_cliente(self, entidad: Cliente) -> None:
        dto = self.mapeador.entidad_a_dto(entidad)
        self.session.delete(dto)
        self.session.commit()