import paho.mqtt.client as mqtt_client

# Server
MQTT_BROKER = "BorkerDomo"
MQTT_PORT   = 1883
KEEP_ALIVE  = 45

# Called on receive logs
def onLog(client, userdata, leve, buffer):
    print("Log: ${buffer}")

def onConnection(client, userdata, flags)