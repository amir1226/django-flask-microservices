
import pika, json
from dotenv import load_dotenv
from os import getenv

load_dotenv()

params = pika.URLParameters(getenv('PIKA_URL'))

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='django_admin', body=json.dumps(body),
                          properties=properties)
    
    