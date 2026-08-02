from pydub import AudioSegment


def convert_ogg_to_wav(input_file, output_file):
    # Load the OGG file
    audio = AudioSegment.from_ogg(input_file)

    # Export as MP3 with desired bitrate
    audio.export(output_file, format="wav")