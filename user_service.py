import time
import hashlib
from fastapi import FastAPI
import logging

logger = logging.getLogger('User_Service')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('user_service.log')
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

app = FastAPI()

def hash_user_info(user_info):
    return hashlib.md5(user_info.encode()).hexdigest()

@app.get("/get_unique_id")
async def get_unique_id():
    user_id = hash_user_info(str(time.time()))
    logger.info(f"User with unique ID {user_id} registered.")
    return {"user_id": user_id}
