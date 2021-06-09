import time
import paho.mqtt.client as paho
broker="broker.hivemq.com"
broker="iot.eclipse.org"
#define callback
def on_message(client, userdata, message):
    time.sleep(1)
    print("received message =",str(message.payload.decode("utf-8")))

client= paho.Client("client-001") 
client.on_message=on_message

print("connecting to broker ",broker)
client.connect("broker.hivemq.com")

client.loop_start() 
print("subscribing ")
client.subscribe("house/bulb1")
time.sleep(2)
print("publishing ")
client.publish("house/bulb1","Hello World")
time.sleep(4)
client.disconnect() 
client.loop_stop() 
