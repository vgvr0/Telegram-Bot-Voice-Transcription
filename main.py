import telebot

from config import tg_token
from handlers import register_handlers

from logger import logger


bot = telebot.TeleBot(tg_token)


logger.info('bot started')
register_handlers(bot)



if __name__ == '__main__':
    bot.infinity_polling()