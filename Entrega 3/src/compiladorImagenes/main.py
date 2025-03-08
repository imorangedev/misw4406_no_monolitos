from flask import Flask

from dotenv import load_dotenv
from sqlalchemy import create_engine
from os import getenv
from sys import argv

from infraestructura.model import db
from config import Config
from infraestructura.consumidores import Consumidor
from infraestructura.model import db


if __name__ == "__main__":
    try:
        # consumer = Consumidor()
        # consumer.start_consuming()

        if argv[1] == "develop":
            load_dotenv(".env.dev")
            db_url = f"sqlite:///microservice_test.db"
            engine = create_engine(db_url)
            db.metadata.create_all(engine)
            consumer = Consumidor("develop")
            consumer.start_consuming()

        else:
            load_dotenv(".env.production")
            database_URI = Config().SQLALCHEMY_DATABASE_URI
            print(database_URI)
            engine = create_engine(database_URI)
            db.metadata.create_all(engine)
            consumer = Consumidor()
            consumer.start_consuming()

    except Exception as e:
        print(f"No se pudo iniciar el consumidor: {e}")