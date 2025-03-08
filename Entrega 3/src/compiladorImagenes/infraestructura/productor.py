import pulsar
from datetime import datetime
from uuid import UUID, uuid4

client = pulsar.Client('pulsar://localhost:6650')

producer = client.create_producer('persistent://public/default/mi-topic')
event_dict = {"id_solicitud": str(uuid4()),
                "id_cliente": "pepeperez123",
                "tipo": "compilacion",
                "servicio": "compilacion_imagenes",
                "imagenes": "[1, 2, 5, 7]",
                "fecha_creacion": datetime.now}

producer.send((str(event_dict)).encode('utf-8'))

print(f'Enviado: Evento Importante')

client.close()