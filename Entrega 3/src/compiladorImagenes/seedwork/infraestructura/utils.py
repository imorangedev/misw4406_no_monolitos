from os import getenv

def broker_host():
    return getenv('BROKER_HOST', default="amqp://guest:guest@us2.pitunnel.net:50513/")

def listar_topicos():
    return {
        'topico_entrada': "DatosDescarga",
        'topico_salida_1': "Compilaciones",
        'topico_salida_2': "Notificaciones"
    } 
