import telebot

from config import token
from bot_tools.handlers import register_handlers


bot = telebot.TeleBot(token)


register_handlers(bot)



if __name__ == '__main__':
    bot.infinity_polling()