import telebot

from config import token


def send_message_to_user(user_id, text):
    bot = telebot.TeleBot(token)


    try:
        bot.send_message(user_id, text)
        print("отправка сообщение пользоватлю: ", user_id)

    except Exception as e:
        print(f"error: {user_id}: {e}")

    print("Г О Т О В О")
