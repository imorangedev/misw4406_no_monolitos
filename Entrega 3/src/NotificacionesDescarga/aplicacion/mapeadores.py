from dominio.entidades import Notificacion
from dominio.repositorios import Mapeador
from dominio.objetos_valor import EstadoNotificacion
from infraestructura.dto import NotificacionDB


class MapeadorNotificacion(Mapeador):
    def entidad_a_dto(self, entidad: Notificacion) -> NotificacionDB:
        return NotificacionDB(
            id_evento=entidad.id_evento,
            id_solicitud=entidad.id_solicitud,
            id_cliente=entidad.id_cliente,
            tipo=entidad.tipo,
            servicio=entidad.servicio,
            imagenes=entidad.imagenes,
            estado=entidad.estado,
            fecha_creacion=entidad.fecha_creacion,
        )

    def dto_a_entidad(self, dto: NotificacionDB) -> Notificacion:
        return Notificacion(
            id_evento=dto.id_evento,
            id_solicitud=dto.id_solicitud,
            id_cliente=dto.id_cliente,
            tipo=dto.tipo,
            servicio=dto.servicio,
            imagenes=dto.imagenes,
            estado=EstadoNotificacion(dto.estado),
            fecha_creacion=dto.fecha_creacion,
        )
