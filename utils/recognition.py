import speech_recognition as sr
from db.db import Users



db = Users()



def voice_to_text(user_id):
    # Transcribe the audio to text

    try:
        recognizer = sr.Recognizer()
        with sr.AudioFile('audio/voice.wav') as source:
            audio_data = recognizer.record(source)


            language = db.get_language(user_id)


            text = recognizer.recognize_google(audio_data, language=language)


        return text

    except Exception as e:
        print(e)
        return "Could not make out the speech."
