from sqlalchemy import Column, String, UUID, Enum
from sqlalchemy.ext.declarative import declarative_base

from dominio.objetos_valor import EstadoCliente, Suscripcion

Base = declarative_base()

class ClienteDB(Base):
    __tablename__ = "clientes"

    id = Column(UUID, primary_key=True)
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    pais = Column(String, nullable=False)
    suscripcion = Column(Enum(Suscripcion), nullable=False)
    estado = Column(Enum(EstadoCliente), nullable=False)