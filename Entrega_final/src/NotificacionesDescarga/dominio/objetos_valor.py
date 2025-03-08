from dataclasses import dataclass
from enum import Enum


@dataclass(frozen=True)
class ObjetoValor: ...

@dataclass(frozen=True)
class EstadoNotificacion(Enum):
    INICIADO = "INICIADO"

