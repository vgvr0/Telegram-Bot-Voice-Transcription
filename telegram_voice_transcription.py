import telebot
from pydub import AudioSegment
import speech_recognition as sr



from commaSetup import fix_punctuation
from config import token



# Set up your Telegram bot token
TOKEN = token
bot = telebot.TeleBot(TOKEN)




def convert_ogg_to_mp3(input_file, output_file):
    # Load the OGG file
    audio = AudioSegment.from_ogg(input_file)

    # Export as MP3 with desired bitrate
    audio.export(output_file, format="wav")


    return 'Done.'





@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    try:
        # Download the voice file
        file_info = bot.get_file(message.voice.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        with open("voice.ogg", 'wb') as f:
            f.write(downloaded_file)

        convert_ogg_to_mp3('voice.ogg', "voice.wav")


        # Transcribe the audio to text
        recognizer = sr.Recognizer()
        with sr.AudioFile('voice.wav') as source:
            audio_data = recognizer.record(source)


            text = recognizer.recognize_google(audio_data, language="en")



        result = fix_punctuation(text) # receive text with punctuation and spelling


        bot.reply_to(message, result)



    except Exception as e:
        bot.reply_to(message, f"Error processing the audio: {e}")

bot.polling()
