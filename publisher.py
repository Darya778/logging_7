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

logger = CustomLogger("Publisher")
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - [%(hostname)s] - %(message)s'))
logger.addHandler(console_handler)

file_handler = logging.FileHandler('publisher_logs.log')  # Добавляем FileHandler для записи в файл
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - [%(hostname)s] - %(message)s'))
logger.addHandler(file_handler)

broker = "broker.emqx.io"

pub_client = mqtt_client.Client()  # Перемещаем создание клиента за пределы функции
pub_client.connect(broker)  # Устанавливаем подключение к брокеру

def publish_message(message):
    pub_client.publish("lab/leds/state", message)
    logger.info(f"Published message: {message}")
