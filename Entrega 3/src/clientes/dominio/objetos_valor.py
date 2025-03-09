from dataclasses import dataclass
from enum import Enum

@dataclass(frozen=True)
class ObjetoValor:
    ...

@dataclass(frozen=True)
class Nombre(ObjetoValor):
    nombre: str

@dataclass(frozen=True)
class Email(ObjetoValor):
    direccion: str

@dataclass(frozen=True)
class EstadoCliente(Enum):
    ACTIVO = "ACTIVO"
    SUSPENDIDO = "SUSPENDIDO"

@dataclass(frozen=True)
class Suscripcion(Enum):
    STANDARD = "STANDARD"
    PRO = "PRO"
    ENTERPRISE = "ENTERPRISE"

@dataclass(frozen=True)
class Pais(ObjetoValor):
    nombre: str