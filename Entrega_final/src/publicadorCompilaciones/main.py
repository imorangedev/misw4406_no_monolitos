import asyncio
import logging
import signal
import sys
from dotenv import load_dotenv

from seedwork.infraestructura.utils import broker_host, listar_topicos
from aplicacion.handlers import HandlerWorker
from infraestructura.schema.comandos import EjecutarCompilacionSchema
from infraestructura.consumidores import suscribirse_a_topico

load_dotenv(".env")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)
handler_worker = HandlerWorker()


async def procesar_mensaje(datos):
    """Función callback para procesar mensajes recibidos"""
    try:
        logger.info(f"Mensaje recibido: {datos}")
        # Procesar mensaje y publicar a los tópicos correspondientes
        await handler_worker.handle_mensaje_entrada(datos)
    except Exception as e:
        logger.error(f"Error procesando el mensaje: {e}")
        raise e


async def consumir():
    """Función principal para consumir mensajes"""
    try:
        # Obtener tópico de entrada
        topicos = listar_topicos()
        cola_entrada = topicos["topico_entrada"]

        # Iniciar suscripción
        print("Suscribiendose al topico")
        await suscribirse_a_topico(
            topico=cola_entrada,
            suscripcion="publicador-compilaciones-sub",
            schema=EjecutarCompilacionSchema,
            fn_callback=procesar_mensaje,
        )
    except Exception as e:
        logger.error(f"Error durante el consumo: {e}")


async def main():
    # Configurar manejadores de señales
    def signal_handler(sig, frame):
        print("Apagando el consumidor")
        logger.info("Señal de interrupción recibida")
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    try:
        await consumir()
    except KeyboardInterrupt:
        logger.info("Interrupción por teclado")
    except Exception as e:
        logger.error(f"Error en el servicio de publicador de compilaciones: {e}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        logger.error(f"No se pudo iniciar el consumidor: {e}")
