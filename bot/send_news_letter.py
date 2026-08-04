import telebot

from config import token


def send_news(users_id, text):
    bot = telebot.TeleBot(token)

    for row in users_id:
        user_id = row[0] if isinstance(row, (tuple, list)) else row

        try:
            bot.send_message(user_id, text)
            print("отправка:", user_id)

        except Exception as e:
            # if user blocked our bot - we don't panick and news_letter don't broke.
            print(f"error: {user_id}: {e}")

    print("Г О Т О В О")
