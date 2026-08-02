


def download_voice_file(bot, message):
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)


    with open("audio/voice.ogg", 'wb') as f:
        f.write(downloaded_file)