import paho.mqtt.client as mqtt
from Topics import topics
from Pusher import push_to_database
from Pusher import init_database_connection

# Constantes utiles pour la connection au server MQTT
MQTT_BROKER = "mqtt.gw.wlan"
MQTT_PORT   = 1883
KEEP_ALIVE  = 45

def on_log(client, userdata, level, buffer):
    """
    Appelée quand un log est recu
    """

    print("Log: " + buffer)

def on_connection(client, userdata, flags, rc):
    """
    Appelée lorsqu'une connection est etablie
    """
    
    print("New connection")

def on_message(client, userdata, message):
    """
    Appelée lorsque qu'une publication est recue
    """

    topic: str = message.topic
    value: str = message.payload.decode()

    push_to_database(topic, value)

def main():
    client: mqtt.Client = mqtt.Client(client_id="Raspberry")

    client.on_message = on_message
    client.on_connect = on_connection
    client.on_log     = on_log

    client.username_pw_set(username="Rasp", password="RaspDomo")
    client.connect(host=MQTT_BROKER, port=MQTT_PORT, keepalive=KEEP_ALIVE)

    # Souscription a tout les topic dans le fichier ./Topics.py
    for topic in topics:
        client.subscribe(topic)

    client.loop_forever()

main()