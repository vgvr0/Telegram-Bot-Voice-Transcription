import speech_recognition as sr


def voice_to_text():
    # Transcribe the audio to text

    try:
        recognizer = sr.Recognizer()
        with sr.AudioFile('audio/voice.wav') as source:
            audio_data = recognizer.record(source)


            text = recognizer.recognize_google(audio_data, language='en')


        return text

    except Exception as e:
        print(e)
        return "Could not make out the speech."
