import time
import hashlib
from fastapi import FastAPI
import logging
import socket

# Logger configuration
logging.basicConfig(level=logging.DEBUG)

class CustomLogger(logging.Logger):
    def makeRecord(self, name, level, fn, lno, msg, args, exc_info, func=None,
                    extra=None, sinfo=None, **kwargs):  # Добавлен **kwargs
        record = super(CustomLogger, self).makeRecord(
            name, level, fn, lno, msg, args, exc_info, func, extra, sinfo, **kwargs
        )
        record.hostname = socket.gethostname()
        return record

logger = CustomLogger("User_Service")
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - [%(hostname)s] - %(message)s'))
logger.addHandler(console_handler)

file_handler = logging.FileHandler('user_service_logs.log')  # Добавляем FileHandler для записи в файл
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - [%(hostname)s] - %(message)s'))
logger.addHandler(file_handler)

app = FastAPI()

@app.get("/")  # Добавляем корневой обработчик
async def root():
    return {"message": "User Service is running"}

def hash_user_info(user_info):
    return hashlib.md5(user_info.encode()).hexdigest()

@app.get("/get_unique_id")
def get_unique_id():
    user_id = hash_user_info(str(time.time()))  # Хэшируем уникальный идентификатор
    logger.info(f"User with unique ID {user_id} registered.")

    return {"user_id": user_id}
