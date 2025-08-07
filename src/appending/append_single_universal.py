from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC



def append_file_metadata_universal(file_path: str, md_type: str, md_text: str):
    if file_path.endswith(".mp3"):
        audio_file = EasyID3(file_path)
    elif file_path.endswith(".flac"):
        audio_file = FLAC(file_path)
    audio_file[md_type] = md_text
    audio_file.save()
