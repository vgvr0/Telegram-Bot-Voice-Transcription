import telebot


from utils.spelling import fix_punctuation
from utils.converter import convert_ogg_to_wav
from utils.recognition import voice_to_text
from utils.download_file import download_voice_file
from utils.remover import remove_audio_files

from config import token



TOKEN = token
bot = telebot.TeleBot(TOKEN)



@bot.message_handler(content_types=['voice'])
def handle_voice(message):


    download_voice_file(bot, message)

    convert_ogg_to_wav('audio/voice.ogg', "audio/voice.wav")


    text = voice_to_text()

    result = fix_punctuation(text) # receive text with punctuation and spelling

    bot.reply_to(message, result)

    remove_audio_files()






if __name__ == '__main__':
    bot.polling()