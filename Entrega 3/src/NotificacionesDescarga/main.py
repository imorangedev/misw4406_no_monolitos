from dotenv import load_dotenv
from sqlalchemy import create_engine

from config import Config
from infraestructura.consumidores import Consumidor
from infraestructura.dto import Base

load_dotenv(".env")

if __name__ == "__main__":
    database_URI = Config().SQLALCHEMY_DATABASE_URI
    print(database_URI)
    engine = create_engine(database_URI)
    Base.metadata.create_all(engine)

    consumidor = Consumidor()
    try:
        consumidor.listen()
    except KeyboardInterrupt:
        consumidor.close()
