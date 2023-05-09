# Template pour la publication sur un topic

import paho.mqtt.client as mqtt

# Server
MQTT_BROKER = "mqtt.gw.wlan"
MQTT_PORT   = 1883
KEEP_ALIVE  = 45

ID          = "Ventilateur"
USERNAME    = "Ventilateur"
PASSWORD    = "/"

def onLog(client, userdata, level, buffer):
    print(buffer)

# Publish data on a specific topic
def publish(client, topic: str, data: any):
    client.publish(topic, data)

def main():
    client = mqtt.Client(client_id=ID)

    client.username_pw_set(username=USERNAME, password=PASSWORD)
    client.connect(host=MQTT_BROKER, port=MQTT_PORT, keepalive=KEEP_ALIVE)

    publish(client, "Maison/Test", "Hello World !")

main()