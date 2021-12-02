
import pika
from dotenv import load_dotenv
from os import getenv

load_dotenv()

params = pika.URLParameters(getenv('PIKA_URL'))

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='flask_main')

def callback(ch, method, properties, body):
    print('Receive in main')
    print(body)

channel.basic_consume(queue='flask_main', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()