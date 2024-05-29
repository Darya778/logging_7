import uvicorn
from publisher import publish_message
from user_service import app as user_service_app

# Запускаем FastAPI приложение User-Service
uvicorn.run(user_service_app, host="localhost", port=8000)

# Пример публикации сообщения через MQTT
publish_message("Message from main.py")
