import json
from infraestructura.despachadores import Despachador
from infraestructura.schema.comandos import (
    SolicitarConsultaCompilacionSchema,
    SolicitarDescargaSchema,
    SolicitarRegistroClienteSchema,
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
            imagenes=json.dumps(cuerpo["imagenes"]),
        )
        return self.despachador.publicar_comando(
            comando,
            self.topicos["topico_servicios_descargas_consultas"],
            schema=SolicitarDescargaSchema,
        )

    def handle_consulta_descarga(self, cuerpo: dict):
        consulta = SolicitarConsultaCompilacionSchema(
            tipo=cuerpo["tipo"],
            servicio=cuerpo["servicio"],
            id_cliente=str(cuerpo["id_cliente"]),
            correo_cliente=cuerpo["correo_cliente"],
            id_consulta=str(cuerpo["id_consulta"]),
        )
        return self.despachador.publicar_consulta(
            consulta,
            self.topicos["topico_servicios_descargas_comandos"],
            schema=SolicitarConsultaCompilacionSchema,
        )

    def handle_comando_crear_cliente(self, cuerpo: dict):
        comando = SolicitarRegistroClienteSchema(
            tipo=cuerpo["tipo"],
            servicio=cuerpo["servicio"],
            correo_cliente=cuerpo["correo_cliente"],
        )
        return self.despachador.publicar_comando(
            comando,
            self.topicos["topico_clientes_comandos"],
            schema=SolicitarRegistroClienteSchema,
        )
