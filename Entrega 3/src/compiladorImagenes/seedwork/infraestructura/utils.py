from os import getenv

def broker_host():
    return getenv(
        "BROKER_HOST", default="pulsar://localhost:6650"
    )

def listar_topicos():
    return {
        'topico_entrada': "persistent://public/default/DatosDescarga",
        'topico_salida_1': "persistent://public/default/Compilaciones",
        'topico_salida_2': "persistent://public/default/Notificaciones"
    } 