import paho.mqtt.client as mqtt

MQTT_SRC_HOST = "192.168.8.130"
MQTT_SRC_PORT = 1883
MQTT_SRC_TOPIC = "/src/+"

MQTT_DST_HOST = "localhost"
MQTT_DST_PORT = 1883


def on_connect(client, userdata, flag, rc):
    client.subscribe(MQTT_SRC_TOPIC)


def on_message(client, userdata, msg):
    dst_client = mqtt.Client()
    dst_client.connect(MQTT_DST_HOST, MQTT_DST_PORT)
    dst_client.publish(msg.topic, msg.payload)
    dst_client.disconnect()


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SRC_HOST, MQTT_SRC_PORT)
client.loop_forever()
