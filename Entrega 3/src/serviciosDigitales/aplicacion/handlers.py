from dominio.comandos import SolicitarConsulta, SolicitarDescarga
from infraestructura.despachadores import Despachador
from seedwork.infraestructura.utils import listar_topicos

class HandlerServiciosDigitales():
    def __init__(self):
        self.despachador = Despachador()
        self.topicos = listar_topicos()

    def handle_solicitud_descarga(self, cuerpo: dict):
        comando = SolicitarDescarga(
            id_cliente=cuerpo['id_cliente'],
            tipo=cuerpo['tipo'],
            servicio=cuerpo['servicio'],
            imagenes=cuerpo['imagenes']
        )
        comando = comando.__dict__
        return self.despachador.publicar_comando(comando, self.topicos['topico_servicios_descargas'])
    
    def handle_consulta_descarga(self, cuerpo: dict):
        consulta = SolicitarConsulta(
            id_cliente=cuerpo['id_cliente'],
            correo_cliente=cuerpo['correo_cliente'],
            tipo=cuerpo['tipo'],
            servicio=cuerpo['servicio'],
            id_consulta=cuerpo['id_consulta']
        )
        consulta = consulta.__dict__
        return self.despachador.publicar_comando(consulta, self.topicos['topico_servicios_descargas'])