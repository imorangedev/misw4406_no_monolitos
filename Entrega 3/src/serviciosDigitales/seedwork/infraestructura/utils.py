from os import getenv

def broker_host():
<<<<<<< Updated upstream
    return getenv('BROKER_HOST', default="amqp://guest:guest@us2.pitunnel.net:57823/")
=======
    return getenv('BROKER_HOST', default="pulsar://127.0.0.1:6650")
>>>>>>> Stashed changes

def listar_topicos():
    return {
        'topico_servicios_descargas': "persistent://public/default/serviciosdigitales"
    }