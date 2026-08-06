from logs.record_log import log_info, log_error

import os



def remove_old_files(ogg_file, wav_file):
    try:
        log_info('remove_old_files')
        os.remove(ogg_file)
        os.remove(wav_file)


    except Exception as e:
        log_error(f'error in remover_files: {e}')
