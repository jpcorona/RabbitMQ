import pika

def setup_direct_queues():
    # Conectar a RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declarar un intercambio directo
    exchange_name = 'direct_exchange'
    channel.exchange_declare(exchange=exchange_name, exchange_type='direct')

    # Declarar colas y enlazarlas al intercambio con claves de routing específicas
    queues = ['tienda', 'compra', 'notificacion']
    for queue in queues:
        channel.queue_declare(queue=queue)
        # En este caso, la clave de routing es el mismo nombre de la cola
        channel.queue_bind(exchange=exchange_name, queue=queue, routing_key=queue)

    print("Colas directas creadas y enlazadas al intercambio.")

    # Cerrar la conexión
    connection.close()

setup_direct_queues()
