import pulsar
from pulsar.schema import AvroSchema

from seedwork.infraestructura.utils import broker_host, listar_topicos
from aplicacion.handlers import HandlerWorker
from infraestructura.schema.comandos import NotificacionDescargaSchema


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

            # Crear consumidor con AvroSchema
            self.consumer = self.client.subscribe(
                self.cola_entrada,
                "notificaciones-descarga-sub",
                consumer_type=pulsar.ConsumerType.Shared,
                schema=AvroSchema(NotificacionDescargaSchema),
            )

        except Exception as e:
            print(f"Error al conectar con el broker: {e}")

    def procesar_mensaje(self, mensaje):
        try:
            # Decodificar el mensaje usando AvroSchema
            msg = AvroSchema(NotificacionDescargaSchema).decode(mensaje.data())
            data = msg.__dict__
            print(f"Mensaje recibido: {data}")

            # Procesar mensaje y agregar a la base de datos
            self.handler.handle_mensaje_entrada(data)

            # Confirmar procesamiento
            self.consumer.acknowledge(mensaje)

        except Exception as e:
            print(f"Error procesando el mensaje: {e}")
            self.consumer.negative_acknowledge(mensaje)

    def listen(self):
        print(f"Esperando mensajes en {self.cola_entrada}. Para salir, presiona CTRL+C")

        while True:
            try:
                mensaje = self.consumer.receive(timeout_millis=3000)
                if mensaje:
                    self.procesar_mensaje(mensaje)
            except pulsar._pulsar.Timeout:
                pass
            except KeyboardInterrupt:
                print("Apagando el consumidor...")
                break
            except Exception as e:
                print(f"Error durante el consumo: {e}")

    def close(self):
        if self.consumer:
            self.consumer.close()
        if self.client:
            self.client.close()
            print("Conexión con el broker cerrada.")
