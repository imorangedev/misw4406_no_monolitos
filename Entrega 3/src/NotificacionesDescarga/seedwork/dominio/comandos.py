from dataclasses import dataclass, field
from datetime import datetime as dt
from uuid import UUID, uuid4

@dataclass
class ComandoDominio():
    _id: UUID = field(init=False, repr=False, hash=True)
    fecha_comando: dt = field(default_factory=dt.now, init=False, repr=False)

    @classmethod
    def siguiente_id(self) -> UUID:
        return uuid4()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id: UUID) -> None:
        self._id = self.siguiente_id()