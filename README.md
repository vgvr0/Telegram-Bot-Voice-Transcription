# Audio to Text Transcription in Telegram Bot

This Python script utilizes the telebot library to create a Telegram bot that can transcribe audio to text using the speech_recognition library.

Requirements

- Python 3.x
- The telebot and speech_recognition libraries (installable via pip)
- A Telegram bot token

Installation

1. Clone this repository or download the script file.

2. Install the dependencies by running the following command in your terminal:
```
    pip install pyTelegramBotAPI SpeechRecognition
```
3. Obtain a token for your Telegram bot by following the instructions in the official Telegram documentation.

Usage

1. Replace "your_token_here" in the code with your Telegram bot token.

2. Run the Python script:
```
    python script_name.py
```
3. Send a voice message to your Telegram bot. The bot will reply with the transcription of the audio.

Notes

- This script utilizes the Google Speech Recognition API, so internet access is required to perform the transcription.
- Ensure you have a good internet connection and that the audio sent to the bot is clear to obtain accurate transcription.
- The script handles errors when processing the audio and will reply with an error message if any issues occur.
