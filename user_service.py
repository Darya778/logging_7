import time
import hashlib
from fastapi import FastAPI

app = FastAPI()

def hash_user_info(user_info):
    return hashlib.md5(user_info.encode()).hexdigest()

@app.get("/get_unique_id")
def get_unique_id():
    user_id = hash_user_info(str(time.time()))  # Хэшируем уникальный идентификатор
    print(f"User with unique ID {user_id} registered.")

    return {"user_id": user_id}
