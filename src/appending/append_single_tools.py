import os
from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC



def append_metadata_file_universal(
    file_path: str,
    md_type: str,
    md_text: str
) -> None:
    # Safe against mac files ugh
    filename = os.path.basename(file_path)
    if filename.startswith("."):
        return

    if file_path.endswith(".mp3"):
        try:
            audio = EasyID3(file_path)
        except Exception as e:
            print(f"Failed to create EasyID3 object. Error: {e}")
            return
    elif file_path.endswith(".flac"):
        try:
            audio = FLAC(file_path)
        except Exception as e:
            print(f"Failed to create FLAC object. Error: {e}")
            return
    audio[md_type] = md_text
    audio.save()
