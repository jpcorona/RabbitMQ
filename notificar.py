import pika

def setup_notification_queue():
    # Conectar a RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declarar un intercambio directo si aún no existe
    exchange_name = 'direct_exchange'
    channel.exchange_declare(exchange=exchange_name, exchange_type='direct')

    # Declarar la cola de notificaciones
    queue_name = 'notificaciones'
    channel.queue_declare(queue=queue_name)

    # Enlazar la cola al intercambio con una clave de routing
    routing_key = 'notificacion'
    channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)

    print("Cola de notificaciones creada y enlazada al intercambio.")

    # Cerrar la conexión
    connection.close()

setup_notification_queue()
