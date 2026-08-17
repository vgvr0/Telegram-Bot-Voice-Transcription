import telebot

from config import tg_token
from bot_tools.handlers import register_handlers


bot = telebot.TeleBot(tg_token)


register_handlers(bot)



if __name__ == '__main__':
    bot.infinity_polling()