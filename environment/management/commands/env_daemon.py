from django.core.management.base import BaseCommand, CommandError
import paho.mqtt.client as mqtt
import time
import datetime
from environment.models import Temperature

BROKER_ADDRESS="92.222.172.12"

def on_connect(client, userdata, flags, rc):
    m="Connected flags"+str(flags)+"result code "\
    +str(rc)+"client1_id  "+str(client)
    print(m)

def on_message(client1, userdata, message):
    measure = float(message.payload.decode("utf-8"))
    if message.topic == 'temperature':
        Temperature(measure=measure).save()
    print(message.topic, datetime.datetime.now().strftime('%D %H:%M:%S'), measure)

class Command(BaseCommand):
    help = 'Populate database'

    def handle(self, *args, **options):
        client1 = mqtt.Client("P1")
        client1.on_connect= on_connect
        client1.on_message=on_message
        client1.connect(BROKER_ADDRESS)

        while True:
            time.sleep(1)
            client1.loop_start()
            client1.subscribe("temperature")
            client1.subscribe("humidity")
