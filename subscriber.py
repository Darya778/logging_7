import paho.mqtt.client as mqtt_client
import logging
import socket

# Logger configuration
logging.basicConfig(level=logging.DEBUG)

class CustomLogger(logging.Logger):
    def makeRecord(self, *args, kwargs):
        record = super(CustomLogger, self).makeRecord(*args, kwargs)
        record.hostname = socket.gethostname()
        return record

logger = CustomLogger("Subscriber")
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - [%(hostname)s] - %(message)s'))
logger.addHandler(console_handler)

file_handler = logging.FileHandler('subscriber_logs.log')  # Добавляем FileHandler для записи в файл
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - [%(hostname)s] - %(message)s'))
logger.addHandler(file_handler)

broker = "broker.emqx.io"

def on_message(client, userdata, message):
    data = str(message.payload.decode("utf-8"))
    logger.info(f"Received message: {data}")

sub_client = mqtt_client.Client()
sub_client.on_message = on_message
sub_client.connect(broker)

# Subscribe to a topic
topic = "lab/leds/state"
sub_client.subscribe(topic)

# Loop to receive messages
sub_client.loop_forever()
