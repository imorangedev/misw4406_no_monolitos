from os import getenv

def broker_host(environment):

    if environment == "dev":
        return getenv(
            'BROKER_HOST', default="pulsar://localhost:6650"
        )
    else:
        return getenv(
            'BROKER_HOST', default="pulsar://127.0.0.1:6650"
        )

def listar_topicos(environment):
    
    if environment == "dev":
        return {
            'topico_entrada': "persistent://public/default/Compilador_imagenes",
        }
    else: 
        return {
            'topico_entrada': "persistent://public/default/Compilador_imagenes",
        } 