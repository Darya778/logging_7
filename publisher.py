import random
import time
import paho.mqtt.client as mqtt_client
import logging
import requests
from fastapi import FastAPI
app = FastAPI()

logger = logging.getLogger("Publisher")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('publisher.log')
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
def register_user():
    response = requests.get("http://localhost:8000/get_unique_id")
    user_id = response.json()["user_id"]
    return user_id

broker = "broker.emqx.io"
pub_client = mqtt_client.Client(register_user())

print("Connecting to broker", broker)
print(pub_client.connect(broker))
logger.debug("Connected to broker")
pub_client.loop_start()
print("Publishing")
logger.info("Started publishing")

for i in range(10):
    state = "on" if random.randint(0, 1) == 0 else "off"
    state = state + "ArtemV"
    logger.debug(f"Published message: {state}")
    print(f"State is {state}")
    pub_client.publish("lab/leds/state", state)
    time.sleep(2)

pub_client.disconnect()
pub_client.loop_stop()
logger.debug("Disconnected from broker")
