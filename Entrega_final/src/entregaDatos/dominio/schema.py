# Para Apache Pulsar
from pulsar.schema import Record, String, Long

# Esquemas de mensajes para Apache Pulsar
class CommandMessage(Record):
    id_solicitud = String()
    fecha_creacion = Long()
    tipo = String()
    servicio = String()
    id_cliente = String()
    data = String()

class CommandOutputMessage(Record):
    id_solicitud = String()
    tipo = String()
    servicio = String()
    fecha_creacion = Long()
    id_cliente = String()
    imagenes = String()

class QueryMessage(Record):
    id_solicitud = String()
    fecha_creacion = Long()
    tipo = String()
    servicio = String()
    id_cliente = String()
    correo_cliente = String()
    data = String()

# Para SQLAlchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Modelo de base de datos para SQLAlchemy
class CompilationModel(Base):
    __tablename__ = "compilaciones"
    id = Column(String, primary_key=True, nullable=False)
    id_archivo = Column(String, nullable=False)
    id_cliente = Column(String, nullable=False)
    id_solicitud = Column(String, nullable=False)
