import pulsar

client = pulsar.Client('pulsar://localhost:6650')

consumer = client.subscribe('persistent://public/default/mi-topic',
                            subscription_name='mi-suscripcion')

while True:
    msg = consumer.receive()
    print(f'Recibido: {msg.data().decode("utf-8")}')
    consumer.acknowledge(msg)

client.close()