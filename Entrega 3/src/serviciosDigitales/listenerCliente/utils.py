from os import getenv

def broker_host():
    return getenv('BROKER_HOST', default="pulsar://127.0.0.1:6650")
    #return getenv('BROKER_HOST', default="amqp://guest:guest@us2.pitunnel.net:46249/")

def listar_topicos():
    return {
        'topico_clientes_consultas': "persistent://public/default/clientesconsultas",
    }