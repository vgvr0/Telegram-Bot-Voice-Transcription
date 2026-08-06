import os


def download_voice_file(bot, user_id, message):
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)


    if not os.path.isdir("audio"):
        os.mkdir('audio')


    with open(f"audio/{user_id}_{message.message_id}.ogg", 'wb') as f:
        f.write(downloaded_file)