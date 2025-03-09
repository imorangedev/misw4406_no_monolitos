import os

from flask import Flask

from dotenv import load_dotenv
from sqlalchemy import create_engine
from os import getenv
from sys import argv

from infraestructura.model import db
from infraestructura.consumidores import Consumidor
from infraestructura.model import db


if __name__ == "__main__":
    try:

        if argv[1] == "develop":
            print('start development environment')
            print(argv[1])
            load_dotenv(".env.dev")
            db_url = f"sqlite:///microservice_test.db"
            engine = create_engine(db_url)
            # db.metadata.create_all(engine)
            consumer = Consumidor(environment=argv[1], engine=engine)
            consumer.start_consuming()

        else:
            load_dotenv(".env")
            DB_NAME = os.environ.get('DATABASE')
            DB_SERVER = os.environ.get('SERVER')
            DB_USER = 'postgres'
            DB_PASSWORD = os.environ.get('PASSWORD')
            database_URI = f"postgresql+pg8000://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}"
            engine = create_engine(database_URI)
            # db.metadata.create_all(engine)
            consumer = Consumidor(environment='prod', engine=engine)
            consumer.start_consuming()

    except Exception as e:
        print(f"No se pudo iniciar el consumidor: {e}")