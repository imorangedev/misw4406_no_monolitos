import pika

import json

import time

from config import Config

def callback(ch, method, properties, body):
    try:
        
        mensaje = json.loads(body)

        print(f"Recibido: {mensaje}")
        print(f"Tipo: {mensaje.get("tipo")}")
        print(f"Correo: {mensaje.get("correo_cliente")}")
        print(f"Recibido: {mensaje}")

        ch.basic_ack(delivery_tag=method.delivery_tag)
        print("Mensaje confirmado (ACK)")

        """ {'fecha_comando': '2025-02-23 19:28:14.342949', 'id_solicitud': 'ae288471-6814-40cd-b057-92650c2a95e1', 'id_cliente': '12b81dae-fc99-4085-8471-947d7b750101', 'correo_cliente': 'jdoe@misouniandes.com', 'tipo': 'Consulta', 'servicio': 'Descargar', 'id_consulta': '5798d00b-52ea-44a5-8600-b52a6ad2955e', 'fecha_creacion': '2025-02-23 19:28:14.342949'} """

        """ {'fecha_comando': '2025-02-23 19:29:11.412446', 'id_solicitud': '1ad59164-97d3-4004-8972-6190423bd1bc', 'id_cliente': '12b81dae-fc99-4085-8471-947d7b750101', 'tipo': 'Comando', 'servicio': 'Descargar', 'imagenes': [1000001, 1000010, 1000100, 1001000, 1010000, 1100000, 1100001, 1100010, 1100100, 1101000, 1110000], 'fecha_creacion': '2025-02-23 19:29:11.412446'} """
    
    except Exception as e:
        print(f"Error procesando mensaje: {e}")
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)
        print("Mensaje reenviado a la cola")


def start_worker():

    BROKER_HOST = Config.BROKER_HOST

    parameters = pika.URLParameters(BROKER_HOST)

    while True:
        try:
            connection = pika.BlockingConnection(parameters)

            channel = connection.channel()

            channel.queue_declare(queue=Config.RABBITMQ_QUEUE, durable=False)

            channel.basic_consume(queue=Config.RABBITMQ_QUEUE, on_message_callback=callback, auto_ack=False)

            print(f"Worker en ejecución, esperando mensajes en la cola '{Config.RABBITMQ_QUEUE}'...")

            channel.start_consuming()

        except Exception as e:
            print(f"Error iniciando el worker: {e}")

            print("Reintentando en 5 segundos...")
            
            time.sleep(5)
