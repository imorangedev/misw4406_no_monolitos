from datetime import datetime as dt
from uuid import UUID, uuid4

print (f'"id_evento": "{str(uuid4())}", "id_solicitud": "{str(uuid4())}", "id_cliente": "{str(uuid4())}", "tipo": "cualquier_tipo", "servicio": "cualquier_servicio", "imagenes": "[1, 2, 5, 7]", "estado": "INICIADO", "fecha_creacion": "{dt.now()}"')