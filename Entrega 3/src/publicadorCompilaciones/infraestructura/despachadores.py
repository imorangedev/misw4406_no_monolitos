import pulsar
import json
from seedwork.infraestructura.utils import broker_host, listar_topicos
from infraestructura.schema.comandos import EjecutarCompilacionSchema
from infraestructura.schema.eventos import CompilacionIniciadaSchema


class Despachador:
    def __init__(self):
        self.client = pulsar.Client(broker_host())
        self.productores = {}

        # Crear productores para cada tópico
        topicos = listar_topicos()
        for key, topico in topicos.items():
            if key == "topico_salida_1":
                # Usar schema para el tópico de comandos
                self.productores[topico] = self.client.create_producer(
                    topico,
                    schema=pulsar.schema.AvroSchema(EjecutarCompilacionSchema),
                    properties={"schema.auto.update": "true"},
                )
            elif key == "topico_salida_2":
                # Usar schema para el tópico de eventos
                self.productores[topico] = self.client.create_producer(
                    topico,
                    schema=pulsar.schema.AvroSchema(CompilacionIniciadaSchema),
                    properties={"schema.auto.update": "true"},
                )
            else:
                self.productores[topico] = self.client.create_producer(topico)

    def _publicar_mensaje(self, mensaje, topico, tipo_mensaje):
        try:
            # Agregar diferenciación de mensaje al contenido
            mensaje_completo = {"tipo_mensaje": tipo_mensaje, "contenido": mensaje}

            # Convertir el mensaje a bytes
            mensaje_bytes = json.dumps(mensaje_completo, default=str).encode("utf-8")

            # Publicar mensaje
            self.productores[topico].send(mensaje_bytes)

            print(
                f"{tipo_mensaje.capitalize()} publicado exitosamente en {topico}: {mensaje}"
            )
            return True
        except Exception as e:
            print(f"Error publicando {tipo_mensaje}: {e}")
            return False

    def publicar_comando(self, mensaje, topico, tipo_mensaje):
        try:
            if topico in self.productores and isinstance(
                self.productores[topico]._schema, pulsar.schema.AvroSchema
            ):
                # Crear instancia del schema
                comando = EjecutarCompilacionSchema(
                    id_solicitud=mensaje["id_solicitud"],
                    id_cliente=mensaje["id_cliente"],
                    tipo=mensaje["tipo"],
                    servicio=mensaje["servicio"],
                    imagenes=json.dumps(mensaje["imagenes"]),
                )
                # Enviar usando el schema
                self.productores[topico].send(comando)
                print(
                    f"{tipo_mensaje.capitalize()} publicado exitosamente en {topico} usando schema: {mensaje}"
                )
                return True
            else:
                # Usar el método tradicional
                return self._publicar_mensaje(mensaje, topico, tipo_mensaje)
        except Exception as e:
            print(f"Error publicando {tipo_mensaje} con schema: {e}")
            return False

    def publicar_evento(self, mensaje, topico, tipo_mensaje):
        try:
            if topico in self.productores and isinstance(
                self.productores[topico]._schema, pulsar.schema.AvroSchema
            ):
                # Crear instancia del schema de evento
                evento = CompilacionIniciadaSchema(
                    id_solicitud=mensaje["id_solicitud"],
                    id_cliente=mensaje["id_cliente"],
                    tipo=mensaje["tipo"],
                    servicio=mensaje["servicio"],
                    imagenes=json.dumps(mensaje["imagenes"]),
                    estado="INICIADO",
                )
                # Enviar usando el schema
                self.productores[topico].send(evento)
                print(
                    f"{tipo_mensaje.capitalize()} publicado exitosamente en {topico} usando schema: {mensaje}"
                )
                return True
            else:
                # Usar el método tradicional
                return self._publicar_mensaje(mensaje, topico, tipo_mensaje)
        except Exception as e:
            print(f"Error publicando {tipo_mensaje} con schema: {e}")
            return False

    def __del__(self):
        # Cerrar conexiones al destruir el objeto
        for productor in self.productores.values():
            productor.close()
        self.client.close()
