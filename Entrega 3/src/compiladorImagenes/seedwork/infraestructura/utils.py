from os import getenv

def broker_host(environment):

    if environment == "develop":
        return getenv(
            'BROKER_HOST', default="pulsar://localhost:6650"
        )
    else:
        return getenv(
            'BROKER_HOST', default="http://35.232.12.233:3000"
        )

def listar_topicos(environment):
    
    if environment == "develop":
        return {
            'topico_salida_1': "persistent://public/default/Compilaciones",
        }
    else: 
        return {
            'topico_salida_1': "persistent://public/default/Compilaciones",
        } 