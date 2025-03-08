import json
from infraestructura.despachadores import Despachador
from seedwork.infraestructura.utils import listar_topicos
from dominio.comandos import EjecutarCompilacion
from dominio.eventos import CompilacionIniciada
from infraestructura.schema.comandos import EjecutarCompilacionSchema
from infraestructura.schema.eventos import CompilacionIniciadaSchema


class HandlerWorker:
    def __init__(self):
        self.despachador = Despachador()
        self.topicos = listar_topicos()

    async def handle_mensaje_entrada(self, cuerpo):
        # Procesar el campo imagenes si viene como string JSON
        # Verificamos si estamos recibiendo un diccionario o un objeto schema
        if hasattr(cuerpo, "__dict__"):
            # Es un objeto schema, convertirlo a diccionario
            if hasattr(cuerpo, "imagenes"):
                imagenes = cuerpo.imagenes
            else:
                imagenes = []

            # Extraer el resto de propiedades
            id_solicitud = getattr(cuerpo, "id_solicitud", None)
            id_cliente = getattr(cuerpo, "id_cliente", None)
            tipo = getattr(cuerpo, "tipo", None)
            servicio = getattr(cuerpo, "servicio", None)
        else:
            # Es un diccionario
            imagenes = cuerpo.get("imagenes", [])
            id_solicitud = cuerpo.get("id_solicitud")
            id_cliente = cuerpo.get("id_cliente")
            tipo = cuerpo.get("tipo")
            servicio = cuerpo.get("servicio")

        # Procesar imagenes si es un string JSON
        if isinstance(imagenes, str):
            try:
                imagenes = json.loads(imagenes)
            except json.JSONDecodeError:
                # Si no es un JSON válido, mantenerlo como está
                pass

        # Crear comando de dominio
        comando = EjecutarCompilacion(
            id_solicitud=id_solicitud,
            id_cliente=id_cliente,
            tipo=tipo,
            servicio=servicio,
            imagenes=imagenes,
        )

        # Crear evento de dominio
        evento = CompilacionIniciada(
            id_solicitud=id_solicitud,
            id_cliente=id_cliente,
            tipo=tipo,
            servicio=servicio,
            imagenes=imagenes,
            estado="INICIADO",
        )

        # Crear instancias de schema para enviar
        comando_schema = EjecutarCompilacionSchema(
            id_solicitud=str(comando.id_solicitud),
            id_cliente=str(comando.id_cliente),
            tipo=comando.tipo,
            servicio=comando.servicio,
            imagenes=(
                json.dumps(comando.imagenes)
                if isinstance(comando.imagenes, (dict, list))
                else comando.imagenes
            ),
        )

        evento_schema = CompilacionIniciadaSchema(
            id_evento=str(evento.id_evento),
            id_solicitud=str(evento.id_solicitud),
            id_cliente=str(evento.id_cliente),
            tipo=evento.tipo,
            servicio=evento.servicio,
            imagenes=(
                json.dumps(evento.imagenes)
                if isinstance(evento.imagenes, (dict, list))
                else evento.imagenes
            ),
            estado=evento.estado,
        )

        # Publicar comando en tópico de compilaciones usando schema
        await self.despachador.publicar_comando(
            comando_schema, self.topicos["topico_salida_1"], EjecutarCompilacionSchema
        )

        # Publicar evento en tópico de notificaciones usando schema
        await self.despachador.publicar_evento(
            evento_schema, self.topicos["topico_salida_2"], CompilacionIniciadaSchema
        )

        return True
