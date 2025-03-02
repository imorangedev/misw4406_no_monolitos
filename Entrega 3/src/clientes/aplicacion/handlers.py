import json
from dominio.entidades import Cliente
from dominio.objetos_valor import EstadoCliente, Suscripcion
from infraestructura.despachadores import Despachador
from infraestructura.repositorios import RepositorioClientes
from infraestructura.schema.comandos import (
    SolicitarRegistroClienteSchema,
    OperacionesClienteSchema
)
from seedwork.infraestructura.utils import listar_topicos

class HandlerClientes:
    def __init__(self):
        self.despachador = Despachador()
        self.repositorio = RepositorioClientes()
        self.topicos = listar_topicos()

    def handle_solicitud_creacion(self, cuerpo: dict):
        nuevo_cliente = Cliente(
            nombre = cuerpo['nombre'],
            email = cuerpo['email'],
            pais = cuerpo['pais'],
            estado = EstadoCliente(cuerpo['Estado']),
            suscripcion = Suscripcion(cuerpo['suscripcion'])
        )
        comando = SolicitarRegistroClienteSchema(
            tipo = cuerpo['tipo'],
            servicio = cuerpo['servicio'],
            correo_cliente = cuerpo['email']
        )
        self.repositorio.crear_cliente(nuevo_cliente)
        self.despachador.publicar_comando(comando, listar_topicos['topico_clientes_eventos'], SolicitarRegistroClienteSchema)

    def handle_solicitud_eliminacion(self, cuerpo: dict):
        comando = OperacionesClienteSchema(
            tipo=cuerpo["tipo"],
            servicio=cuerpo["servicio"],
            id_cliente=str(cuerpo["id_cliente"]),
        )
        cliente = self.repositorio.obtener_cliente_por_id(cuerpo['id_cliente'])
        self.repositorio.eliminar_cliente(cliente)
        self.despachador.publicar_comando(comando, listar_topicos['topico_clientes_eventos'], OperacionesClienteSchema)


    def handle_consulta_cliente(self, cuerpo: dict):
        consulta = OperacionesClienteSchema(
            tipo=cuerpo["tipo"],
            servicio=cuerpo["servicio"],
            id_cliente=str(cuerpo["id_cliente"]),
        )
        self.despachador.publicar_consulta(consulta, listar_topicos['topico_clientes_eventos'], OperacionesClienteSchema)
        cliente = self.repositorio.obtener_cliente_por_id(cuerpo['id_cliente'])
        return json.dumps(cliente.__dict__)