from dataclasses import dataclass, field

from dominio.objetos_valor import EstadoCliente, Email, Nombre, Pais, Suscripcion
from seedwork.dominio.entidades import Entidad

@dataclass
class Cliente(Entidad):
    nombre: Nombre = field(default_factory=Nombre)
    email: Email = field(default_factory=Email)
    pais: Pais = field(default_factory=Pais)
    suscripcion: Suscripcion = field(default_factory=Suscripcion)
    estado: EstadoCliente = field(default_factory=EstadoCliente)