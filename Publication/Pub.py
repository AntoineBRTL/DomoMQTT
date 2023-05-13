# Template pour la publication sur un topic

import paho.mqtt.client as mqtt

# Constantes utiles pour la connection au server MQTT
MQTT_BROKER = "mqtt.gw.wlan"
MQTT_PORT   = 1883
KEEP_ALIVE  = 45

# Changer le username, l'id et le mot de passe (On peut garder "/" pour le mot de passe)
ID          = "Ventilateur"
USERNAME    = "Ventilateur"
PASSWORD    = "/"

def on_log(client: mqtt.Client, userdata, level, buffer):
    """
    Appelée quand un log est recu
    """
    print(buffer)

def main():
    client: mqtt.Client = mqtt.Client(client_id=ID)

    client.username_pw_set(username=USERNAME, password=PASSWORD)
    client.connect(host=MQTT_BROKER, port=MQTT_PORT, keepalive=KEEP_ALIVE)

    client.on_log = on_log

    client.publish("Maison/Test", "Hello World !")

main()