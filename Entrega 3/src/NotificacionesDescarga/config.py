from os import getenv


class Config:
    DB_USER = getenv("USER")
    DB_PASSWORD = getenv("PASSWORD")
    DB_SERVER = getenv("SERVER")
    DB_NAME = getenv("DATABASE")

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql+pg8000://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
