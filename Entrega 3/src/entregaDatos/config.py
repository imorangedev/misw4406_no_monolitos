from dotenv import load_dotenv
from os import getenv



load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql+pg8000://{getenv("DB_USER","postgres")}:{getenv("DB_PASSWORD","cuartetodevops")}@{getenv("DB_SERVER","34.45.41.49")}/{getenv("DB_NAME","postgres")}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BROKER_HOST = getenv(
        'BROKER_HOST')
    BROKER_COMMAND_TOPIC = getenv(
        'BROKER_COMMAND_TOPIC')
    BROKER_QUERY_TOPIC = getenv('BROKER_QUERY_TOPIC')
    BROKER_COMMAND_OUTPUT_TOPIC = getenv("BROKER_COMMAND_OUTPUT_TOPIC")
    BROKER_COMMAND_SUBCRIPTION = getenv('BROKER_COMMAND_SUBCRIPTION')
    BROKER_QUERY_SUBCRIPTION = getenv('BROKER_QUERY_SUBCRIPTION')
    EMAIL_API_KEY=getenv("EMAIL_API_KEY")
    EMAIL_API_SECRET=getenv("EMAIL_API_SECRET")
    FROM_EMAIL=getenv("FROM_EMAIL")