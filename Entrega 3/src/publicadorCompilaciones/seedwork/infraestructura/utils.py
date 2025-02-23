from os import getenv

def broker_host():
    return getenv(
        "BROKER_HOST", default="amqp://guest:guest@http://us2.pitunnel.net:37471/#/"
    )

def listar_topicos():
    return {
        'topico_entrada': "DatosDescarga",
        'topico_salida_1': "Compilaciones",
        'topico_salida_2': "Notificaciones"
    } 
