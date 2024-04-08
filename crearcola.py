import pika

# Conectarse a RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declarar la cola 'tienda'
channel.queue_declare(queue='tienda')

# Cerrar la conexión
connection.close()
