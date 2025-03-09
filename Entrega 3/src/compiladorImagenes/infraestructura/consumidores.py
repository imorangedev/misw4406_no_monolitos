import pulsar
import json

from seedwork.infraestructura.utils import broker_host, listar_topicos
from aplicacion.handlers import HandlerWorker

class Consumidor:
    def __init__(self, environment: str, engine):
        self.client = None
        self.consumer = None
        self.environment = environment
        self.handler = HandlerWorker(self.environment, engine)

        # Establecer conexión con el broker
        try:
            broker_url = broker_host(self.environment)
            
            if not broker_url:
                raise ValueError("El host del broker no es válido.")

            self.client = pulsar.Client(broker_url)

            # Obtener tópico de entrada
            topicos = listar_topicos(self.environment)
            print(topicos)
            self.cola_entrada = topicos["topico_salida_1"]

            # Crear consumidor
            self.consumer = self.client.subscribe(
                self.cola_entrada,
                subscription_name='mi-suscripcion'
            )

        except Exception as e:
            print(f"Error al conectar con el broker: {e}")

    def procesar_mensaje(self, mensaje):
        try:
            # Decodificar el mensaje
            datos = json.loads(mensaje.data().decode("utf-8"))
            print(f"Mensaje recibido: {datos}")

            # Procesar mensaje y publicar a los tópicos correspondientes
            self.handler.handle_mensaje_entrada(datos)

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