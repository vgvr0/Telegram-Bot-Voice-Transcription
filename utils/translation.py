import json
from db.db import Users
from logs.record_log import log_info, log_error

db = Users()

def translate(user_id, key):
    try:
        log_info('translate we are looking for a translation into the desired language')

        with open("messages.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        language_code = db.get_language(user_id)


        return data[f'{key}{language_code}']



    except Exception as e:
        log_error(f'error translation.py: {e}')