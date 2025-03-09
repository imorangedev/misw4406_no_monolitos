from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from uuid import UUID

from dominio.repositorios import LogsRepositorio
from dominio.entidades import Logs
from infraestructura.model import LogsImagecompiler
from aplicacion.mapeadores import MapeadorLogs

class LogsRepositorioSQL(LogsRepositorio):
    def __init__(self, session: Session):
        self.session = session
        self._mapeador = MapeadorLogs()

    def agregar(self, log: Logs):
        dto = self._mapeador.entidad_a_dto(log)
        self.session.add(dto)
        self.session.commit()