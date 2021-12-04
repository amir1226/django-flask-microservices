import pika, json, os, django
from dotenv import load_dotenv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_admin.settings")
django.setup()

from products.models import Product

load_dotenv()

params = pika.URLParameters(os.getenv('PIKA_URL'))

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='django_admin')

def callback(ch, method, properties, body):
    print('Receive in admin')
    data = json.loads(body)
    print(data)
    product = Product.objects.get(id=data)
    product.likes = product.likes + 1
    product.save()
    print('Product likes increased')

channel.basic_consume(queue='django_admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()