import os


def remove_old_files(ogg_file, wav_file):
    try:
        os.remove(ogg_file)
        os.remove(wav_file)

    except Exception as e:
        print(e)