from os import getenv
class Config:
    SQLALCHEMY_DATABASE_URI = f"pg8000://{getenv('USER')}:{getenv('PASSWORD')}@{getenv('SERVER')}/{getenv('DATABASE')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BROKER_HOST = getenv('BROKER_HOST',default="amqps://tscpcxhq:T5Bpe4qh9VoD8LR0Pe1V-pgiC5PL9ZNO@leopard.lmq.cloudamqp.com/tscpcxhq/")
    RABBITMQ_INPUT_QUEUE  = getenv('RABBITMQ_QUEUE',default="serviciosdigitales")
    RABBITMQ_OUTPUT_QUEUE  = getenv('RABBITMQ_QUEUE',default="DatosDescarga")