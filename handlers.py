from audio_processing.audio_recognition import recognition
from googletrans import Translator


from db import Users


import os

from logger import logger

db = Users()




def register_handlers(bot):
    @bot.message_handler(commands=['start'])
    def welcome(message):
        user_id = message.from_user.id
        name = message.from_user.first_name
        username = message.from_user.username
        language_code = message.from_user.language_code

        lang = language_code[:2] if language_code else 'en'

        logger.info('command start')
        db.add_user(user_id, name, username, language_code)

        text_to_translate = (
            f"👋 Hi, {name}!"
            f"\nI’m a bot you can forward 🎙 voice messages from friends to, and I’ll send you the transcription. "
            f"\nThis bot is open source. Link to the code below 👇\n\n"
            f'<b><a href="https://github.com/platilich/Telegram-Bot-Voice-Transcription">GitHub</a></b>'

        )

        try:
            translator = Translator()
            result = translator.translate(text_to_translate, dest=lang)
            clean_result = result.text


        except Exception as e:
            logger.error(f"error translate: {e}")
            clean_result = text_to_translate



        bot.send_message(
            message.chat.id,
            clean_result,
            disable_web_page_preview=True,
            parse_mode='HTML'
        )



    @bot.message_handler(content_types=['voice'])
    def handle_voice(message):
        user_id = message.from_user.id
        file_info = bot.get_file(message.voice.file_id) # file_info
        downloaded_file = bot.download_file(file_info.file_path) # downloaded file



        logger.info('voice handler')



        try:
            logger.info('creating the audios directory')
            os.mkdir('audios')

        except Exception as e:
            logger.info(f'the directory is already there: {e}')


        with open(f"audios/{user_id}_{message.message_id}.ogg", 'wb') as f:
            f.write(downloaded_file)


        text = recognition(f'audios/{user_id}_{message.message_id}.ogg')



        try:
            bot.reply_to(
                message,
                f'<code>{text}</code>\n\n\n<b><a href="https://github.com/platilich/Telegram-Bot-Voice-Transcription">GitHub</a></b>',
                disable_web_page_preview=True,
                parse_mode='HTML'
                )


        except Exception as e:
            logger.error(f'error when sending a message to the user: {e}')


        os.remove(f"audios/{user_id}_{message.message_id}.ogg")