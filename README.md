# Telegram Bot — Voice Transcription

A Telegram bot that transcribes voice messages into text.

You can forward voice messages from friends (or send your own), and the bot replies with the transcription. It supports multiple interface languages and uses AI to fix punctuation and spelling.

## Features

- Transcribes Telegram voice messages (`.ogg`) to text
- Multi-language UI and speech recognition (English, Kazakh, Russian)
- Automatic punctuation and spelling fixes via Ollama (`llama3.2:3b`)
- Simple setup with the included installer

## Requirements

- Python 3.x
- Internet connection (Google Speech Recognition API + Ollama)
- A Telegram bot token from [@BotFather](https://t.me/BotFather)
- macOS / Linux (the installer uses a Unix-style setup)

## Quick start (recommended)

1. Clone the repository:

```bash
git clone https://github.com/platilich/Telegram-Bot-Voice-Transcription.git
cd Telegram-Bot-Voice-Transcription
```

2. Run the installer:

```bash
python3 installer.py
```

3. When prompted, paste your bot token from BotFather.

The installer will:

- create a virtual environment (`venv/`)
- install Python dependencies from `requirements.txt`
- install [Ollama](https://ollama.com)
- download the `llama3.2:3b` model
- save your token to `config.py`

4. Start the bot:

```bash
source venv/bin/activate
python main.py
```

Or without activating the venv:

```bash
venv/bin/python main.py
```

5. Open Telegram, find your bot, send `/start`, pick a language, then send or forward a voice message.

## Manual installation

If you prefer to set things up yourself:

1. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Install [Ollama](https://ollama.com) and pull the model:

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3.2:3b
```

4. Create `config.py` in the project root:

```python
token = 'YOUR_BOT_TOKEN_HERE'
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
- Қазақ (Kazakh)
- Русский (Russian)

## How it works

1. The bot downloads the voice message
2. Converts `.ogg` → `.wav`
3. Transcribes audio with Google Speech Recognition (using the user’s selected language)
4. Improves punctuation/spelling with Ollama (`llama3.2:3b`)
5. Replies with the cleaned text

## Notes

- Internet access is required for speech recognition and for Ollama (if the model is served remotely; local Ollama still needs the model installed).
- Clear audio gives better results.
- If speech cannot be recognized, the bot replies with an error message.
- Keep your bot token private — do not commit `config.py` with a real token.

## Project structure

```
.
├── main.py              # Bot entry point
├── installer.py         # One-step setup script
├── config.py            # Bot token (created by installer)
├── requirements.txt
├── bot/
│   ├── handlers.py      # Commands and voice handling
│   ├── sender_message.py
│   └── translation.py
├── utils/
│   ├── recognition.py   # Speech-to-text
│   ├── converter.py     # OGG → WAV
│   ├── spelling.py      # Punctuation / spelling via Ollama
│   └── ...
└── db/
    └── db.py            # User language preferences
```

## License

See [LICENSE](LICENSE).
