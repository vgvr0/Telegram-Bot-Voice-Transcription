import telebot
import json

from utils.spelling import fix_punctuation
from utils.converter import convert_ogg_to_wav
from utils.recognition import voice_to_text
from utils.download_file import download_voice_file
from utils.remover import remove_audio_files
from bot.keyboard import default_keyboard

from db.db import Users

from bot.translation import translate


db = Users()
db.init_db()




def register_handlers(bot):
    @bot.message_handler(commands=['start'])
    def welcome(message):
        user_id = message.from_user.id
        name = message.from_user.first_name
        username = message.from_user.username


        db.manage_user(user_id, name, username)


        if db.get_language(user_id) is None:
            bot.send_message(
                message.chat.id,
                text=f"👋 Hi, <b>{name}</b>! I’m a bot you can forward 🎙 voice messages from friends to, and I’ll send you the transcription. Select the bot's interface language and the language to be used for transcribing voice messages.\n\nChoice your language 👇",
                reply_markup=default_keyboard(),
                parse_mode='HTML'

            )


        else:
            answer = translate(user_id, 'welcome_msg_')

            bot.send_message(
                message.chat.id,
                text=answer,
                parse_mode='HTML'

            )






    @bot.message_handler(commands=['language'])
    def change_language(message):
        user_id = message.from_user.id
        answer = translate(user_id, 'select_language_')

        bot.send_message(message.chat.id, text=answer, reply_markup=default_keyboard())




    @bot.message_handler(content_types=['voice'])
    def handle_voice(message):
        user_id = message.from_user.id


        download_voice_file(bot, message)

        convert_ogg_to_wav('audio/voice.ogg', "audio/voice.wav")

        text = voice_to_text(user_id)

        result = fix_punctuation(text)  # receive text with punctuation and spelling

        bot.reply_to(message, result)

        remove_audio_files()







    @bot.message_handler(content_types=['text'])
    def text_input(message):
        user_id = message.from_user.id

        text = message.text



        if text == '🇺🇸 English':
            db.set_language(user_id, 'en-US')
            bot.send_message(message.chat.id, '⚙️ The language is installed', reply_markup=telebot.types.ReplyKeyboardRemove())




        elif text == '🇰🇿 Қазақ':
            db.set_language(user_id, 'kk-KZ')
            bot.send_message(message.chat.id, '⚙️ Тіл орнатылған', reply_markup=telebot.types.ReplyKeyboardRemove())




        elif text == '🇷🇺 Русский':
            db.set_language(user_id, 'ru-RU')
            bot.send_message(message.chat.id, '⚙️ Язык установлен', reply_markup=telebot.types.ReplyKeyboardRemove())




        else:
            answer = translate(user_id, 'unknow_text_', )

            bot.send_message(message.chat.id, answer, reply_markup=telebot.types.ReplyKeyboardRemove())