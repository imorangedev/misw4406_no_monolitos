from dominio.entidades import Logs
from dominio.repositorios import Mapeador
from infraestructura.model import LogsImagecompiler

class MapeadorLogs(Mapeador):
    def entidad_a_dto(self, entidad: Logs) -> LogsImagecompiler:
        return LogsImagecompiler(
            id=entidad.id,
            id_cliente=entidad.id_cliente,
            id_solicitud=entidad.id_solicitud,
            id_zip_file=entidad.id_zip_file,
            # tipo=entidad.tipo,
            # servicio=entidad.servicio,
            # imagenes=entidad.imagenes,
            # estado=entidad.estado,
            # fecha_creacion=entidad.fecha_creacion,
        )