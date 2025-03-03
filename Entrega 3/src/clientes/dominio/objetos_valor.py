from dataclasses import dataclass
from enum import Enum

@dataclass(frozen=True)
class ObjetoValor:
    ...

@dataclass(frozen=True)
class Nombre(ObjetoValor):
    nombres: str
    apellidos: str

@dataclass(frozen=True)
class Email(ObjetoValor):
    direccion: str
    dominio: str

@dataclass(frozen=True)
class EstadoCliente(Enum):
    ACTIVO = "Activo"
    SUSPENDIDO = "Suspendido"

@dataclass(frozen=True)
class Suscripcion(Enum):
    STANDARD = "Standard"
    PRO = "Pro"
    ENTERPRISE = "Enterprise"

@dataclass(frozen=True)
class Pais(ObjetoValor):
    nombre: str