from audio_processing.text_cleaner import fix_punctuation
from audio_processing.file_converter import convert_ogg_to_wav
from audio_processing.audio_recognition import voice_to_text
from audio_processing.file_downloader import download_voice_file

from db.db import Users
from bot_tools.message_sender import send_message_with_keyboard, send_message_without_keyboard
from utils.translation import translate
from utils.remover_files import remove_old_files




db = Users()
db.init_db()




def register_handlers(bot):
    @bot.message_handler(commands=['start'])
    def welcome(message):
        user_id = message.from_user.id
        name = message.from_user.first_name

        db.add_user(user_id)


        if db.get_language(user_id) is None:
            send_message_with_keyboard(bot, message, f"👋 Hi, <b>{name}</b>! I’m a bot you can forward 🎙 voice messages from friends to, and I’ll send you the transcription. Select the bot's interface language and the language to be used for transcribing voice messages.\n\nChoice your language 👇")


        else:
            answer = translate(user_id, 'welcome_msg_')

            send_message_without_keyboard(bot, message, answer.replace('name', name))






    @bot.message_handler(commands=['language'])
    def change_language(message):
        user_id = message.from_user.id

        answer = translate(user_id, 'select_language_')

        send_message_with_keyboard(bot, message, answer)




    @bot.message_handler(content_types=['voice'])
    def handle_voice(message):
        user_id = message.from_user.id


        download_voice_file(bot, user_id, message)

        convert_ogg_to_wav(f'audio/{user_id}_{message.message_id}.ogg', f"audio/{user_id}_{message.message_id}.wav")

        text = voice_to_text(user_id, message)


        result = fix_punctuation(text)  # receive text with punctuation and spelling

        remove_old_files(f"audio/{user_id}_{message.message_id}.ogg", f"audio/{user_id}_{message.message_id}.wav")

        bot.reply_to(message, result)





    @bot.message_handler(content_types=['text'])
    def text_input(message):
        user_id = message.from_user.id

        text = message.text



        if text == '🇺🇸 English':
            db.set_language(user_id, 'en-US')
            send_message_without_keyboard(bot, message, '⚙️ The language is installed')


        elif text == '🇪🇸 España':
            db.set_language(user_id, 'es-ES')
            send_message_without_keyboard(bot, message, '⚙️ El idioma está instalado')



        elif text == '🇷🇺 Русский':
            db.set_language(user_id, 'ru-RU')
            send_message_without_keyboard(bot, message, "⚙️ Язык установлен")



        elif text == '🇰🇿 Қазақ':
            db.set_language(user_id, 'kk-KZ')
            send_message_without_keyboard(bot, message, '⚙️ Тіл орнатылған')



        else:
            answer = translate(user_id, 'unknow_text_', )
            send_message_without_keyboard(bot, message, answer)