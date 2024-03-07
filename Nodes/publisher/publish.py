import pika
import os
import time

time.sleep(10)  # Esperar a que el contenedor de RabbitMQ se inicialice
rabbitmq_host = os.getenv('RABBITMQ_HOST')
rabbitmq_credentials = pika.PlainCredentials(os.getenv('RABBITMQ_USERNAME'), os.getenv('RABBITMQ_PASSWORD'))
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host, credentials=rabbitmq_credentials))
channel = connection.channel()
channel.queue_declare(queue='hello')

while True:
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello World!')
    print(" [x] Sent 'Hello World!'")
    time.sleep(1)

connection.close()
