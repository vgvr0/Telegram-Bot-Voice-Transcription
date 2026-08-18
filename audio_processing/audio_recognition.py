from faster_whisper import WhisperModel
from logger import logger

def recognition(file_path):
    try:
        logger.info('audio_recognition | recognition')

        model = WhisperModel(
            "small",
            device="cpu",
            compute_type="int8",
            num_workers=1
        )

        segments, info = model.transcribe(file_path, language=None)

        text_list = []
        for segment in segments:
            text_list.append(segment.text)

        full_text = " ".join(text_list)


        return full_text


    except Exception as e:
        logger.error(f'audio_recognition | error: {e}')