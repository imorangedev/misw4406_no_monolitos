from infraestructura.despachadores import Despachador
from seedwork.infraestructura.utils import topico_servicios

class HandlerServiciosDigitales():
    def __init__(self):
        self.despachador = Despachador()

    def handle_solicitud_descarga(self, comando):
        self.despachador.publicar_comando(comando, topico_servicios)