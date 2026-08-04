import json
from database.db import Users


db = Users()

def translate(user_id, key):
    with open("messages.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    language_code = db.get_language(user_id)


    return data[f'{key}{language_code}']