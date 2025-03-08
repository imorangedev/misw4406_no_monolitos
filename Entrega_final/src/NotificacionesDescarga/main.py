import asyncio
import logging
import signal
import sys
from infraestructura.consumidores import Consumidor
from config import Config

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


async def main():
    consumidor = Consumidor()

    def signal_handler(sig, frame):
        logger.info("Señal de interrupción recibida")
        consumidor.cerrar()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    try:
        await consumidor.iniciar()
    except KeyboardInterrupt:
        logger.info("Interrupción por teclado")
    except Exception as e:
        logger.error(f"Error en el servicio de notificaciones: {e}")
    finally:
        consumidor.cerrar()


if __name__ == "__main__":
    asyncio.run(main())
