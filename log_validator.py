import re
import datetime

def extract_timestamp(log_message):
    # Извлекает метку времени из строки лога.
    pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'
    timestamp_match = re.search(pattern, log_message)
    if timestamp_match:
        return datetime.datetime.strptime(timestamp_match.group(), "%Y-%m-%d %H:%M:%S")
    return None

def validate_log_order(log_file):
    # Проверяет порядок записей в файле логов.
    with open(log_file, 'r') as file:
        lines = file.readlines()

    user_registered = False
    last_event_time = None

    for line in lines:
        timestamp = extract_timestamp(line)
        if timestamp:
            if "registered" in line:
                user_registered = True

            if user_registered and last_event_time:
                if timestamp < last_event_time:
                    print(f"Invalid log order: {line}")
                    return False

            last_event_time = timestamp
    print("Log order is correct.")
    return True

log_file_path = 'subscriber_logs.log'
validate_log_order(log_file_path)
log_file_path = 'publisher_logs.log'
validate_log_order(log_file_path)
log_file_path = 'user_service_logs.log'
validate_log_order(log_file_path)
