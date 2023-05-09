import paho.mqtt.client as mqtt_client
from Topics import topics

# Server
MQTT_BROKER = "mqtt.gw.wlan"
MQTT_PORT   = 1883
KEEP_ALIVE  = 45

# Appelée lors de logs
def onLog(client, userdata, level, buffer):
    print("Log: ${buffer}")

# Appelée lors de la connection d'un client
def onConnection(client, userdata, flags, rc):
    print("New connection")

# Appelée lorsque qu'un message est reçu
def onMessage(client, userdata, message):
    print(message.topic, message.payload)

# Main 
def main():
    client = mqtt_client.Client(client_id="Raspberry")

    client.on_message = onMessage
    client.on_connect = onConnection
    client.on_log     = onLog

    client.username_pw_set(username="Rasp", password="RaspDomo")
    client.connect(host=MQTT_BROKER, port=MQTT_PORT, keepalive=KEEP_ALIVE)

    # Sub to all topics
    for topic in topics:
        client.subscribe(topic)

    client.loop_forever()

main()