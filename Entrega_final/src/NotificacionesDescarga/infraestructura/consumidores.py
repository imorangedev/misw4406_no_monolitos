import asyncio
import logging
import aiopulsar
import pulsar, _pulsar
from pulsar.schema import AvroSchema

from seedwork.infraestructura.utils import broker_host, listar_topicos
from aplicacion.handlers import HandlerWorker
from infraestructura.schema.comandos import NotificacionDescargaSchema

logger = logging.getLogger(__name__)


async def suscribirse_a_topico(
    topico: str,
    suscripcion: str,
    schema,
    tipo_consumidor: pulsar.ConsumerType = pulsar.ConsumerType.Shared,
    fn_callback=None,
):
    try:
        async with aiopulsar.connect(broker_host()) as cliente:
            async with cliente.subscribe(
                topico,
                consumer_type=tipo_consumidor,
                subscription_name=suscripcion,
                schema=AvroSchema(schema),
            ) as consumidor:
                while True:
                    logging.info(
                        f"Esperando mensajes en {topico}. Para salir, presiona CTRL+C"
                    )
                    mensaje = await consumidor.receive()
                    datos = mensaje.value()
                    logger.info(f"Evento recibido: {datos}")

                    # Si se proporciona una función de callback, ejecutarla
                    if fn_callback:
                        await fn_callback(datos)

                    await consumidor.acknowledge(mensaje)

    except Exception as e:
        logger.error(f"ERROR: Suscribiéndose al tópico de eventos! {e}")


class Consumidor:
    def __init__(self):
        self.handler = HandlerWorker()
        self.running = True

    async def iniciar(self):
        # Obtener tópico de entrada
        topicos = listar_topicos()
        cola_entrada = topicos["topico_entrada"]

        print("Suscribiendose al topico")

        try:
            # Suscribirse al tópico y procesar mensajes
            await suscribirse_a_topico(
                topico=cola_entrada,
                suscripcion="notificaciones-descarga-sub",
                schema=NotificacionDescargaSchema,
                fn_callback=self.procesar_mensaje,
            )
        except Exception as e:
            logger.error(f"Error durante la suscripción: {e}")

    async def procesar_mensaje(self, datos):
        try:
            logger.info(f"Mensaje recibido: {datos}")

            # Procesar mensaje y agregar a la base de datos
            await self.handler.handle_mensaje_entrada(datos)

        except Exception as e:
            logger.error(f"Error procesando el mensaje: {e}")
            raise e

    def cerrar(self):
        self.running = False
        logger.info("Consumidor cerrado correctamente.")
