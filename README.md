# Telegram Bot — Voice Transcription

A Telegram bot that transcribes voice messages into text.

Forward voice messages from friends (or send your own), and the bot replies with the transcription.

---

## Features

- Converts Telegram voice messages to text
- Support 99 languages
- Temporary audio files are deleted after processing


---

## How it works

```
Voice message (.ogg)
        ↓
   Download
        ↓
   Faster_whisper (audio to text, support 99 languages)
        ↓
  Reply with text
```

---

## Requirements

| Dependency | Purpose |
| --- | --- |
| Python 3.10+ | bot and admin panel |
| [Telegram Bot Token](https://t.me/BotFather) | Telegram Bot API |
| macOS / Linux | recommended environment |

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/platilich/Telegram-Bot-Voice-Transcription.git
cd Telegram-Bot-Voice-Transcription
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


### 4. Configuration
Create `config.py` in the project root:

```python
tg_token = 'your_token_from_bot_father'
```



## Commands and usage

| Action | Description                        |
| --- |------------------------------------|
| `/start` | Launch the bot                     |
| Voice message | Bot replies with the transcription |


## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).



## Attribution

This project was rewritten from scratch, inspired by: https://github.com/vgvr0/Telegram-Bot-Voice-Transcription