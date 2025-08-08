from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC



def append_metadata_file_universal(file_path: str, md_type: str, md_text: str):
    # print("file_path type: " + str(type(file_path)) + ", value: " + file_path)
    # print("md_type type: " + str(type(md_type)) + ", value: " + md_type)
    # print("md_text type: " + str(type(md_text)) + ", value: " + md_text)
    if file_path.endswith(".mp3"):
        audio_file = EasyID3(file_path)
    elif file_path.endswith(".flac"):
        audio_file = FLAC(file_path)
    audio_file[md_type] = md_text
    audio_file.save()
