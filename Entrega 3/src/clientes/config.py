from os import getenv
class Config:
    SQLALCHEMY_DATABASE_URI = f"postgresql+pg8000://{getenv('USER')}:{getenv('PASSWORD')}@{getenv('SERVER')}/{getenv('DATABASE')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False