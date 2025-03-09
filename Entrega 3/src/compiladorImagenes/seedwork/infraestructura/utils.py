import os
from os import getenv

def broker_host(environment):

    if environment == "develop":
        return getenv(
            'BROKER_HOST', default="pulsar://localhost:6650"
        )
    else:
        return getenv(
            'BROKER_HOST', default="pulsar://localhost:6650"
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