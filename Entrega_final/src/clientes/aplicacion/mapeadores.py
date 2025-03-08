from dominio.entidades import Cliente
from dominio.repositorios import Mapeador
from dominio.objetos_valor import Email, EstadoCliente, Nombre, Pais, Suscripcion
from infraestructura.dto import ClienteDB

class MapeadorCliente(Mapeador):
    def entidad_a_dto(self, entidad: Cliente) -> ClienteDB:
        return ClienteDB(
            id = entidad.id,
            nombre = entidad.nombre,
            email = entidad.email,
            pais = entidad.pais,
            suscripcion = entidad.suscripcion,
            estado = entidad.estado
        )
    
    def dto_a_entidad(self, dto: ClienteDB):
        return Cliente(
            id = dto.id,
            nombre = Nombre(dto.nombre),
            email = Email(dto.email),
            pais = Pais(dto.pais),
            suscripcion = Suscripcion(dto.suscripcion.value),
            estado = EstadoCliente(dto.estado.value)
        )