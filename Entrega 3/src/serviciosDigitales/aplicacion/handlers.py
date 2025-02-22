from infraestructura.despachadores import Despachador
from seedwork.infraestructura.utils import listar_topicos

class HandlerServiciosDigitales():
    def __init__(self):
        self.despachador = Despachador()
        self.topicos = listar_topicos()

    def handle_solicitud_descarga(self, comando: dict):
        self.despachador.publicar_comando(comando, self.topicos['topico_servicios_descargas'])