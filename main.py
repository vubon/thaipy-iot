import time
import json

import config
from lib import aws_iot
from lib.dht11 import DHT11Sensor
from msg import message
from utils.wifi import connect_to_wifi
from utils.blink import blink

# Initialize AWS IoT client
mqtt_client = aws_iot.AwsIoTClient(
    endpoint=config.AWS_ENDPOINT,
    client_id=config.AWS_CLIENT_ID,
    cert_path=config.DEVICE_CERT_PATH,
    key_path=config.DEVICE_KEY_PATH
)
# set message handler function
mqtt_client.set_msg_handler(message)

# Initialize DHT11 sensor on pin 15
dht_sensor = DHT11Sensor(pin=15)


# Initialize and connect to AWS IoT Core
def connect_to_aws():
    print("Connecting to AWS IoT Core...")
    mqtt_client.initialize()
    mqtt_client.connect()
    mqtt_client.subscribe(config.DATA_SUBSCRIBE)


def loop_forever():
    """
    :description: Mainly this function maintenance of functions
    :functionality: Publish data to subscribe MQTT Client.
    :params: None
    :raise: If any function can't perform. It could raise. But there is no self raise case
    :return: None
    :rtype: None
    """
    connect_to_wifi(config.WIFI_SSID, config.WIFI_PASSWORD)
    connect_to_aws()

    try:
        while True:
            temperature = dht_sensor.read_temperature_humidity()
            print("Sensor data: ", temperature)
            # Publish sensor data to AWS IoT
            mqtt_client.publish(config.TEMPERATURE_TOPIC, json.dumps(temperature))

            # Check for incoming MQTT messages
            mqtt_client.check_for_messages()

            # Blink Led
            blink(1)

            # Sleep time for next reading
            time.sleep(15)
    except KeyboardInterrupt:
        mqtt_client.disconnect()


loop_forever()
