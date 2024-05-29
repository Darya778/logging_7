import re
import datetime


def extract_timestamp(log_message):
    pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'
    timestamp_match = re.search(pattern, log_message)
    if timestamp_match:
        return datetime.datetime.strptime(timestamp_match.group(), "%Y-%m-%d %H:%M:%S")
    return None


def validate_log_order(log_file):
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

print("\ncommon.log")
validate_log_order("common.log")
print("\npublisher.log")
validate_log_order("publisher.log")
print("subscriber.log")
validate_log_order("subscriber.log")
print("user_service.log")
validate_log_order("user_service.log")
