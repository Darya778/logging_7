import platform
import time
import paho.mqtt.client as mqtt_client
import logging
import requests

logger = logging.getLogger("Subscriber")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('subscriber.log')
file_handler.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)
common_file_handler = logging.FileHandler('common.log')
common_file_handler.setLevel(logging.DEBUG)
common_file_handler.setFormatter(formatter)
logger.addHandler(common_file_handler)

broker = "broker.emqx.io"
def register_user():
    response = requests.get("http://localhost:8000/get_unique_id")
    user_id = response.json()["user_id"]
    return user_id
def on_message(client, userdata, message):
    data = str(message.payload.decode("utf-8"))
    logger.info(f"Received message: {data}")

sub_client = mqtt_client.Client("http://localhost:8000/get_unique_id")
sub_client.on_message = on_message
sub_client.connect(broker)

topic = "lab/leds/state"
logger.info(f"Running on {platform.node()}")
print("Connecting to broker", broker)
sub_client.connect(broker)
logger.debug("Connected to broker")
sub_client.loop_start()
logger.info("Started subscribing")

sub_client.subscribe("lab/leds/state")
while True:
    time.sleep(1000)
client.disconnect()
client.loop_stop()
logger.debug("Disconnected from broker")
