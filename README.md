# Telegram Bot — Voice Transcription

A Telegram bot that transcribes voice messages into text.

Forward voice messages from friends (or send your own), and the bot replies with the transcription. It supports multiple interface languages and uses a local LLM via Ollama to fix punctuation and capitalization.

---

## Features

- Converts Telegram voice messages to text
- Multilingual interface and speech recognition: English, Spanish, Kazakh, Russian
- Automatic correction of punctuation and capital letters using Ollama (`llama3.2:3b`)
- SQLite user database (language, transcription counter, ban status)
- Temporary audio files are deleted after processing


---

## How it works

```
Voice message (.ogg)
        ↓
   Download
        ↓
  Convert → .wav  (pydub / ffmpeg)
        ↓
 Google Speech Recognition  (user language)
        ↓
 Ollama llama3.2:3b  (punctuation & capitalization)
        ↓
  Reply with text
```

---

## Requirements

| Dependency | Purpose |
| --- | --- |
| Python 3.10+ | bot and admin panel |
| [Telegram Bot Token](https://t.me/BotFather) | Telegram Bot API |
| [Ollama](https://ollama.com) + `llama3.2:3b` | punctuation cleanup |
| Internet | Google Speech Recognition API |
| **ffmpeg** | OGG → WAV conversion via pydub |
| macOS / Linux | recommended environment |

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/platilich/Telegram-Bot-Voice-Transcription.git
cd NoCloud-Voice-Bot
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. Install ffmpeg

```bash
# Ubuntu / Debian
sudo apt install ffmpeg


# macOS
brew install ffmpeg
```

### 5. Install Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Make sure Ollama is running (`ollama serve` or the system service).  
You can pull the model manually, or let the bot do it on first start:

```bash
ollama pull llama3.2:3b
```

### 6. Configuration
Create `config.py` in the project root:

```python
token = "YOUR_BOT_TOKEN_FROM_BOTFATHER"
```

---- 

## Running
To launch, run the command:

```bash
python main.py
```


## Commands and usage

| Action | Description |
| --- | --- |
| `/start` | Register and choose interface / recognition language |
| `/language` | Change language later |
| `/admin` | Open admin panel link (admin only) |
| Voice message | Bot replies with the transcription |

### Supported languages

| Language | Code |
| --- | --- |
| English | `en-US` |
| Español | `es-ES` |
| Қазақ | `kk-KZ` |
| Русский | `ru-RU` |

The selected language is used both for the bot UI and for Google Speech Recognition.

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).



## Attribution

This project was rewritten from scratch, inspired by: https://github.com/vgvr0/Telegram-Bot-Voice-Transcription