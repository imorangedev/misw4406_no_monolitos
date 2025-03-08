from dotenv import load_dotenv
from infraestructura.consumidores import ConsumidorCliente

load_dotenv('.env')

if __name__ == '__main__':
    consumidor = ConsumidorCliente()
    try:
        consumidor.listen()
    except KeyboardInterrupt:
        consumidor.close()