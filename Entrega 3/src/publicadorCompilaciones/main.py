import pika
import json
from seedwork.infraestructura.utils import broker_host, listar_topicos
from aplicacion.handlers import HandlerIntermediario

class Consumidor:
    def __init__(self):
        self.connection = None
        self.channel = None
        self.handler = HandlerIntermediario()
        
        # Establecer conexión con el broker
        try:
            broker_url = broker_host()
            if not broker_url:
                raise ValueError("El host del broker no es válido.")

            self.connection = pika.BlockingConnection(pika.URLParameters(broker_url))
            self.channel = self.connection.channel()
            
            # Declarar cola de entrada
            topicos = listar_topicos()
            self.cola_entrada = topicos['topico_entrada']
            self.channel.queue_declare(queue=self.cola_entrada)
            
        except pika.exceptions.AMQPConnectionError as e:
            print(f"Error al conectar con el broker: {e}")

    def callback(self, ch, method, properties, body):
        try:
            mensaje = json.loads(body)
            print(f"Mensaje recibido: {mensaje}")
            
            # Procesar mensaje y publicar a los tópicos correspondientes
            self.handler.handle_mensaje_entrada(mensaje)
            
            # Confirmar procesamiento
            ch.basic_ack(delivery_tag=method.delivery_tag)
            
        except json.JSONDecodeError as e:
            print(f"Error decodificando el mensaje JSON: {e}")
            ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)
        except Exception as e:
            print(f"Error procesando el mensaje: {e}")
            ch.basic_nack(delivery_tag=method.delivery_tag)

    def start_consuming(self):
        print(f"Esperando mensajes en {self.cola_entrada}. Para salir, presiona CTRL+C")
        
        try:
            self.channel.basic_consume(
                queue=self.cola_entrada,
                on_message_callback=self.callback,
                auto_ack=False
            )
            
            self.channel.start_consuming()
            
        except KeyboardInterrupt:
            print("Apagando el consumidor...")
        except Exception as e:
            print(f"Error durante el consumo: {e}")
        finally:
            if self.connection and self.connection.is_open:
                self.connection.close()
                print("Conexión con el broker cerrada.")

if __name__ == "__main__":
    try:
        consumer = Consumidor()
        consumer.start_consuming()
    except Exception as e:
        print(f"No se pudo iniciar el consumidor: {e}") 
