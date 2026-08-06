from logs.record_log import log_info, log_error
import os


def download_voice_file(bot, user_id, message):
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    try:
        log_info('creating an audio folder, a file file_downlaoder.py')
        if not os.path.isdir("audio"):
            os.mkdir('audio')


    except Exception as e:
        log_error(f'error when creating the audio directory in the file_downloader file: {e}')



    try:
        log_info('download the audio message folder, the file_downloaded file.')

        with open(f"audio/{user_id}_{message.message_id}.ogg", 'wb') as f:
            f.write(downloaded_file)


    except Exception as e:
        log_error(f'error when saving the ogg file in the file_downloader file: {e}')
