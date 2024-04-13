import telebot
import speech_recognition as sr

# Set up your Telegram bot token
TOKEN = "your_token_here"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    try:
        # Download the voice file
        file_info = bot.get_file(message.voice.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        # Transcribe the audio to text
        recognizer = sr.Recognizer()
        with sr.AudioFile(downloaded_file) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data, language="en")

        # Send the transcription back to the user
        bot.reply_to(message, f"Transcription: {text}")
    except Exception as e:
        bot.reply_to(message, f"Error processing the audio: {e}")

bot.polling()
