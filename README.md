# logging_7

**Как запустить:**

1. **Запустите `subscriber.py`:**  Этот файл будет работать в фоновом режиме и слушать сообщения от MQTT-брокера.
   * `user_service_app` будет доступно по адресу `http://localhost:8000/get_unique_id`.
2. **Запустите `main.py`:**  Это запустит FastAPI приложение и отправит тестовое сообщение через MQTT.
3. **Проверьте логи:**  В консоли вы должны увидеть сообщения о получении и отправке данных.
   * Проверьте файлы `subscriber_logs.log`, `publisher_logs.log` и `user_service_logs.log` для детальной информации о работе каждого компонента.
4. **Запустите `log_validator.py`:** Чтобы проверить порядок записей в файле логов.
