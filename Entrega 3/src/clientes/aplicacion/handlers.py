import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

from config import Config
from dominio.entidades import Cliente
from dominio.objetos_valor import EstadoCliente, Suscripcion
from infraestructura.dto import Base
from infraestructura.despachadores import Despachador
from infraestructura.repositorios import RepositorioClientesSQLAlchemy
from infraestructura.schema.comandos import (
    SolicitarRegistroClienteSchema,
    ConsultaClienteSchema
)
from seedwork.infraestructura.utils import listar_topicos

class HandlerClientes:
    def __init__(self):
        database_URI = Config().SQLALCHEMY_DATABASE_URI
        self.engine = create_engine(database_URI)
        Base.metadata.create_all(self.engine)
        session = sessionmaker(bind=self.engine)()
        self.despachador = Despachador()
        self.repositorio = RepositorioClientesSQLAlchemy(session)
        self.topicos = listar_topicos()

    def handle_solicitud_creacion(self, cuerpo: dict):
        nuevo_cliente = Cliente(
            nombre = cuerpo['nombre'],
            email = cuerpo['email'],
            pais = cuerpo['pais'],
            estado = EstadoCliente(cuerpo['estado'].upper()).value,
            suscripcion = Suscripcion(cuerpo['suscripcion'].upper()).value
        )
        comando = SolicitarRegistroClienteSchema(
            tipo = cuerpo['tipo'],
            servicio = cuerpo['servicio'],
            correo_cliente = cuerpo['email']
        )
        try:
            self.repositorio.crear_cliente(nuevo_cliente)
        except IntegrityError:
            pass
        self.despachador.publicar_comando(comando, listar_topicos()['topico_clientes_eventos'], SolicitarRegistroClienteSchema)

    def handle_consulta_cliente(self, cuerpo: dict):
        cliente = self.repositorio.obtener_cliente_por_id(cuerpo['id_cliente'].strip())
        consulta = ConsultaClienteSchema(
            id = cuerpo['id_cliente'].strip(),
            nombre = cliente.nombre.nombre,
            email = cliente.email.direccion,
            estado = cliente.estado.name,
            tipo = cuerpo['tipo'],
            servicio = cuerpo['servicio'],
            data = cuerpo['data']
        )
        self.despachador.publicar_consulta(consulta, listar_topicos()['topico_clientes_consultas'], ConsultaClienteSchema)        
        return json.dumps(consulta.__dict__)