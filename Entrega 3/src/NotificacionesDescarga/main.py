import pulsar
import json
from seedwork.infraestructura.utils import broker_host, listar_topicos
from aplicacion.handlers import HandlerWorker


class Consumidor:
    def __init__(self):
        self.client = None
        self.consumer = None
        self.handler = HandlerWorker()

        # Establecer conexión con el broker
        try:
            broker_url = broker_host()
            if not broker_url:
                raise ValueError("El host del broker no es válido.")

            self.client = pulsar.Client(broker_url)

            # Obtener tópico de entrada
            topicos = listar_topicos()
            self.cola_entrada = topicos["topico_entrada"]

            # Crear consumidor
            self.consumer = self.client.subscribe(
                self.cola_entrada,
                "notificaciones-descarga-sub",
                consumer_type=pulsar.ConsumerType.Shared,
            )

        except Exception as e:
            print(f"Error al conectar con el broker: {e}")

    def procesar_mensaje(self, mensaje):
        try:
            # Decodificar el mensaje
            datos = json.loads(mensaje.data().decode("utf-8"))
            print(f"Mensaje recibido: {datos}")

            # Extraer el contenido del mensaje
            contenido = datos.get("contenido", datos)

            # Procesar mensaje y agregar a la base de datos
            self.handler.handle_mensaje_entrada(contenido)

            # Confirmar procesamiento
            self.consumer.acknowledge(mensaje)

        except json.JSONDecodeError as e:
            print(f"Error decodificando el mensaje JSON: {e}")
            self.consumer.negative_acknowledge(mensaje)
        except Exception as e:
            print(f"Error procesando el mensaje: {e}")
            self.consumer.negative_acknowledge(mensaje)

    def start_consuming(self):
        print(f"Esperando mensajes en {self.cola_entrada}. Para salir, presiona CTRL+C")

        try:
            while True:
                mensaje = self.consumer.receive()
                self.procesar_mensaje(mensaje)

        except KeyboardInterrupt:
            print("Apagando el consumidor...")
        except Exception as e:
            print(f"Error durante el consumo: {e}")
        finally:
            if self.consumer:
                self.consumer.close()
            if self.client:
                self.client.close()
                print("Conexión con el broker cerrada.")


if __name__ == "__main__":
    try:
        consumer = Consumidor()
        consumer.start_consuming()
    except Exception as e:
        print(f"No se pudo iniciar el consumidor: {e}")
