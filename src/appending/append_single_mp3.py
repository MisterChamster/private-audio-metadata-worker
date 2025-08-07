from mutagen.easyid3 import EasyID3



def append_file_metadata_mp3(file_path: str, md_type: str, md_text: str):
    audio_file = EasyID3(file_path)
    audio_file[md_type] = md_text
    audio_file.save()
