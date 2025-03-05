import json
from infraestructura.despachadores import Despachador
from infraestructura.schema.comandos import (
    SolicitarConsultaCompilacionSchema,
    SolicitarDescargaSchema,
    SolicitarRegistroClienteSchema,
    SolicitarConsultaClienteSchema
)
from seedwork.infraestructura.utils import listar_topicos


class HandlerServiciosDigitales:
    def __init__(self):
        self.despachador = Despachador()
        self.topicos = listar_topicos()

    def handle_solicitud_descarga(self, cuerpo: dict):
        comando = SolicitarDescargaSchema(
            tipo=cuerpo["tipo"],
            servicio=cuerpo["servicio"],
            id_cliente=str(cuerpo["id_cliente"]),
            data=json.dumps(cuerpo["data"]),
        )
        return self.despachador.publicar_comando(
            comando,
            self.topicos["topico_servicios_descargas_comandos"],
            schema=SolicitarDescargaSchema,
        )

    def handle_consulta_descarga(self, cuerpo: dict):
        consulta = SolicitarConsultaCompilacionSchema(
            tipo=cuerpo["tipo"],
            servicio=cuerpo["servicio"],
            id_cliente=str(cuerpo["id_cliente"]),
            correo_cliente=cuerpo["correo_cliente"],
            id_consulta=str(cuerpo["data"]),
        )
        return self.despachador.publicar_consulta(
            consulta,
            self.topicos["topico_servicios_descargas_consultas"],
            schema=SolicitarConsultaCompilacionSchema,
        )

    def handle_comando_crear_cliente(self, body: dict):
        comando = SolicitarRegistroClienteSchema(
            nombre = body['nombre'],
            email= body['email'],
            pais = body['pais'],
            estado = body['estado'],
            suscripcion = body['suscripcion'],
            tipo = body['tipo'],
            servicio = body['servicio']
        )
        return self.despachador.publicar_comando(
            comando,
            self.topicos["topico_clientes_comandos"],
            schema=SolicitarRegistroClienteSchema,
        )
    
    def handle_consulta_cliente(self, cuerpo):
        consulta = SolicitarConsultaClienteSchema(
            id_cliente = cuerpo['id_cliente'],
            tipo = cuerpo['tipo'],
            servicio = cuerpo['servicio'],
            data = cuerpo['data']
        )
        return self.despachador.publicar_consulta(
            consulta,
            self.topicos["topico_clientes_solicitudes_consulta"],
            SolicitarConsultaClienteSchema
        )