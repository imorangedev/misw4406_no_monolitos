import pulsar
from pulsar.schema import AvroSchema, Record, String, Long
from pulsar.exceptions import PulsarException
import time
import uuid
from seedwork.infraestructura.utils import broker_host
from aplicacion.handlers import HandlerWorker


# Definición del esquema Avro
class EjecutarCompilacionSchema(Record):
    id_solicitud = String()
    tipo = String()
    servicio = String()
    fecha_creacion = Long()
    id_cliente = String()
    imagenes = String()


class Productor:
    def __init__(self):
        self.client = None
        self.productor = None
        self.handler = HandlerWorker()

        # Establecer conexión con el broker
        try:
            broker_url = broker_host()
            if not broker_url:
                raise ValueError("El host del broker no es válido.")

            self.client = pulsar.Client(broker_url)

            # Crear un productor utilizando el esquema Avro
            self.productor = self.client.create_producer(
                "persistent://public/default/DatosDescargaTestSaga2",
                schema=AvroSchema(EjecutarCompilacionSchema)
            )

        except Exception as e:
            print(f"Error al conectar con el broker: {e}")

    def enviar_mensaje(self, mensaje):
        try:
            print(f"Enviando mensaje: {mensaje}")
            self.productor.send(mensaje)
            print("Mensaje enviado exitosamente.")
        except PulsarException as e:
            print(f"Error al enviar el mensaje: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")


if __name__ == "__main__":
    # Crear una instancia del productor
    productor = Productor()

    # Crear el mensaje utilizando el esquema Avro
    mensaje = EjecutarCompilacionSchema(
        id_solicitud="b1b81dae-fc99-4085-8471-947d7b750101",
        id_cliente="12b81dae-fc99-4085-8471-947d7b750101",
        tipo="Comando",
        servicio="Descargar",
        imagenes="1000001, 1000010, 1000100, 1001000, 1010000, 1100000, 1100001, 1100010, 1100100, 1101000, 1110000",
    )

    # Enviar el mensaje utilizando el esquema Avro
    productor.enviar_mensaje(mensaje)

    # Cerrar la conexión del cliente
    productor.client.close()
