import telebot

from config import token
from utils.handlers import register_handlers



TOKEN = token
bot = telebot.TeleBot(TOKEN)

register_handlers(bot)


if __name__ == '__main__':
    bot.infinity_polling()