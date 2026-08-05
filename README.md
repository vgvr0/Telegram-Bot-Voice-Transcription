# Telegram Bot — Voice Transcription

A Telegram bot that transcribes voice messages into text.

You can forward voice messages from friends (or send your own), and the bot replies with the transcription. It supports multiple interface languages and uses AI to fix punctuation and spelling.


## Features

- Transcribes Telegram voice messages to text
- Multi-language UI and speech recognition (English, Kazakh, Russian, Spanish)
- Automatic punctuation and spelling fixes via Ollama (`llama3.2:3b`)


## Requirements

- Python 3.x
- Internet connection (Google Speech Recognition API + Ollama)
- A Telegram bot token from [@BotFather](https://t.me/BotFather)
- macOS / Linux (the installer uses a Unix-style setup)



## Manual installation

1. Clone the repository:

```bash
git clone https://github.com/platilich/Telegram-Bot-Voice-Transcription.git
cd Telegram-Bot-Voice-Transcription
```


2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3Install dependencies:

```bash
pip install -r requirements.txt
```

4. Install [Ollama](https://ollama.com) and pull the model:

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3.2:3b
```

5. Create `config.py` in the project root:
Run config_build.py it's help you hash your login and password

```python
token = 'YOUR_BOT_TOKEN_HERE'

adminID = 123456789
SECRET = "long_your_generated_secret"
LOGIN = hashed_login
PASSWORD = hashed_password


```

5. Run the bot:

```bash
python main.py
```

## Usage

| Command / action | Description |
| --- | --- |
| `/start` | Register and choose the interface language |
| `/language` | Change language later |
| Voice message | Bot replies with the transcription |

Supported languages for the bot UI and recognition:

- English
- Español (Spanish)
- Қазақ (Kazakh)
- Русский (Russian)


## How it works

1. The bot downloads the voice message
2. Converts `.ogg` → `.wav`
3. Transcribes audio with Google Speech Recognition (using the user’s selected language)
4. Improves punctuation/spelling with Ollama (`llama3.2:3b`)
5. Replies with the cleaned text

## Notes

- Clear audio gives better results.
- If speech cannot be recognized, the bot replies with an error message.
- Keep your bot token, secret, login, password private - DON'T COMMIT `config.py` with a real data.


## License


See [LICENSE](LICENSE).