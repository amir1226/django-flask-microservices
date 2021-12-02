
import pika
from dotenv import load_dotenv
from os import getenv

load_dotenv()

params = pika.URLParameters(getenv('PIKA_URL'))

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='flask_main', body='hello flask')
    
    