import asyncio
import logging
import aiopulsar
import pulsar, _pulsar
from pulsar.schema import AvroSchema, Record
from seedwork.infraestructura.utils import broker_host


async def suscribirse_a_topico(
    topico: str,
    suscripcion: str,
    schema: Record,
    tipo_consumidor: _pulsar.ConsumerType = _pulsar.ConsumerType.Shared,
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
                    logging.info(f"Evento recibido: {datos}")

                    if fn_callback:
                        await fn_callback(datos)

                    await consumidor.acknowledge(mensaje)

    except Exception as e:
        logging.error(f"ERROR: Suscribiéndose al tópico de eventos! {e}")
