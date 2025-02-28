import pika
import json
from seedwork.infraestructura.utils import broker_host, listar_topicos

class Despachador:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.URLParameters(broker_host()))
        self.channel = self.connection.channel()

        topicos = listar_topicos()
        for key in topicos:
            self.channel.queue_declare(topicos[key])

    def publicar_mensaje(self, mensaje, topico, tipo_mensaje):
        try:
            # Agregar diferenciación de mensaje al contenido
            mensaje_completo = {"tipo_mensaje": tipo_mensaje, "contenido": mensaje}

            self.channel.basic_publish(
                exchange="",
                routing_key=topico,
                body=json.dumps(mensaje_completo, default=str),
            )
            print(
                f"{tipo_mensaje.capitalize()} publicado exitosamente en {topico}: {mensaje}"
            )
            return True
        except Exception as e:
            print(f"Error publicando {tipo_mensaje}: {e}")
            return False
