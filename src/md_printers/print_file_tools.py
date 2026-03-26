from pathlib import Path
from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC
from mutagen.oggvorbis import OggVorbis



def print_all_metadata_file(file_path: Path) -> None:
    extension = file_path.suffix

    if extension == ".mp3":
        try:
            audio = EasyID3(file_path)
        except Exception as e:
            print(f"Failed to create EasyID3 object. Error: {e}")
            return

    elif extension == ".flac":
        try:
            audio = FLAC(file_path)
        except Exception as e:
            print(f"Failed to create FLAC object. Error: {e}")
            return

    elif extension == ".ogg":
        try:
            audio = OggVorbis(file_path)
        except Exception as e:
            print(f"Failed to create OggVorbis object. Error: {e}")
            return

    if audio is None:
        print(f"Failed to load file: {file_path}")
        return

    max_len = len('tracknumber')
    for key in audio:
        addstr = (max_len-len(key)) * " "
        print(f"{key}:{addstr} '{audio[key][0]}'")


def print_appendable_metadata_file(file_path: Path) -> None:
    extension = file_path.suffix

    if extension == ".mp3":
        try:
            audio = EasyID3(file_path)
        except Exception as e:
            print(f"Failed to create EasyID3 object. Error: {e}")
            return

    elif extension == ".flac":
        try:
            audio = FLAC(file_path)
        except Exception as e:
            print(f"Failed to create FLAC object. Error: {e}")
            return

    elif extension == ".ogg":
        try:
            audio = OggVorbis(file_path)
        except Exception as e:
            print(f"Failed to create OggVorbis object. Error: {e}")
            return

    if audio is None:
        print(f"Failed to load file: {file_path}")
        return

    specific_md = ['album', 'title', 'artist', 'tracknumber', 'date']
    max_len = len('tracknumber')
    for key in specific_md:
        addstr = (max_len-len(key)) * " "
        if key in audio:
            print(f"{key}:{addstr} '{audio[key][0]}'")
        else:
            print(f"{key}:{addstr} Unavailable")


def print_specific_metadata_file(file_path: Path, md_name: str) -> None:
    extension = file_path.suffix

    if extension == ".mp3":
        try:
            audio = EasyID3(file_path)
        except Exception as e:
            print(f"Failed to create EasyID3 object. Error: {e}")
            return

    elif extension == ".flac":
        try:
            audio = FLAC(file_path)
        except Exception as e:
            print(f"Failed to create FLAC object. Error: {e}")
            return

    elif extension == ".ogg":
        try:
            audio = OggVorbis(file_path)
        except Exception as e:
            print(f"Failed to create OggVorbis object. Error: {e}")
            return

    if audio is None:
        print(f"Failed to load file: {file_path}")
        return

    if md_name in audio:
        print(f"{md_name}: '{audio[md_name][0]}'")
    else:
        print(f"{md_name}: Unavailable")
