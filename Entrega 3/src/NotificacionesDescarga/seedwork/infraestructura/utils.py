from os import getenv

def broker_host():
    return getenv('BROKER_HOST', default="pulsar://127.0.0.1:6650")

def listar_topicos():
    return {
        'topico_entrada': "persistent://public/default/Notificaciones",
    }
