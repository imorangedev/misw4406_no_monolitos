from os import getenv

def broker_host():
    return getenv('BROKER_HOST', default='"amqp://guest:guest@localhost:5672/"')

def listar_topicos():
    return {
        'topico_servicios_descargas': "serviciosdigitales-descargas"
    }