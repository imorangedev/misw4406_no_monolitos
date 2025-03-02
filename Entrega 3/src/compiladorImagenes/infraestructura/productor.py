import pulsar

client = pulsar.Client('pulsar://localhost:6650')

producer = client.create_producer('persistent://public/default/mi-topic')

producer.send('{"ids_imagenes": "[1, 2, 5, 7]", "otro_comando": "otro comando blabla"}'.encode('utf-8'))
print(f'Enviado: Evento Importante')

client.close()