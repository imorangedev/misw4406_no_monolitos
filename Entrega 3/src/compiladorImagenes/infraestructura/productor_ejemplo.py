import pulsar
from datetime import datetime
from uuid import UUID, uuid4

client = pulsar.Client('pulsar://localhost:6650')

producer = client.create_producer("persistent://public/default/Compilaciones")
event_dict = f'"id_solicitud": "{str(uuid4())}", "id_cliente": "{str(uuid4())}", "tipo": "compilacion", "servicio": "compilacion_imagenes", "imagenes": "[1, 2, 5, 7]", "fecha_creacion": "{datetime.now}"'

print(event_dict)

producer.send(('{'+event_dict+'}').encode('utf-8'))

print(f'Enviado: Evento Importante')

client.close()