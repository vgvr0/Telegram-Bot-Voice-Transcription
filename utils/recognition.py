import speech_recognition as sr
from db.db import Users
from utils.remover import remove_audio_files

db = Users()



def voice_to_text(user_id):
    # Transcribe the audio to text

    try:
        recognizer = sr.Recognizer()
        with sr.AudioFile('audio/voice.wav') as source:
            audio_data = recognizer.record(source)


            language = db.get_language(user_id)


            text = recognizer.recognize_google(audio_data, language=language)


        remove_audio_files()

        return text

    except Exception as e:
        remove_audio_files()
        return "Could not make out the speech."
