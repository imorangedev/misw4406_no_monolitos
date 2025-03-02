from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from uuid import UUID

from dominio.repositorios import NotificacionRepositorio
from dominio.entidades import Notificacion
from infraestructura.dto import NotificacionDB
from aplicacion.mapeadores import MapeadorNotificacion


class NotificacionRepositorioSQL(NotificacionRepositorio):
    def __init__(self, session: Session):
        self.session = session
        self._mapeador = MapeadorNotificacion()

    def agregar(self, notificacion: Notificacion):
        dto = self._mapeador.entidad_a_dto(notificacion)
        self.session.add(dto)
        self.session.commit()
