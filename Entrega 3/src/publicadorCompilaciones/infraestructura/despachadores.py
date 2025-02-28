import pulsar
import json
from seedwork.infraestructura.utils import broker_host, listar_topicos


class Despachador:
    def __init__(self):
        self.client = pulsar.Client(broker_host())
        self.productores = {}
        
        # Crear productores para cada tópico
        topicos = listar_topicos()
        for key, topico in topicos.items():
            self.productores[topico] = self.client.create_producer(topico)

    def _publicar_mensaje(self, mensaje, topico, tipo_mensaje):
        try:
            # Agregar diferenciación de mensaje al contenido
            mensaje_completo = {
                "tipo_mensaje": tipo_mensaje,
                "contenido": mensaje
            }
            
            # Convertir el mensaje a bytes
            mensaje_bytes = json.dumps(mensaje_completo, default=str).encode('utf-8')
            
            # Publicar mensaje
            self.productores[topico].send(mensaje_bytes)
            
            print(f"{tipo_mensaje.capitalize()} publicado exitosamente en {topico}: {mensaje}")
            return True
        except Exception as e:
            print(f"Error publicando {tipo_mensaje}: {e}")
            return False

    def publicar_comando(self, mensaje, topico, tipo_mensaje):
        return self._publicar_mensaje(mensaje, topico, tipo_mensaje)

    def publicar_evento(self, mensaje, topico, tipo_mensaje):
        return self._publicar_mensaje(mensaje, topico, tipo_mensaje)

    def __del__(self):
        # Cerrar conexiones al destruir el objeto
        for productor in self.productores.values():
            productor.close()
        self.client.close()
