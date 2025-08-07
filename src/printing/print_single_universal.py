from src.printing.print_single_mp3 import print_specific_metadata_mp3
from src.printing.print_single_flac import print_specific_metadata_flac
from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC



def print_all_metadata_single(file_path: str) -> None:
    try:
        if file_path.endswith(".mp3"):
            audio = EasyID3(file_path)
        elif file_path.endswith(".flac"):
            audio = FLAC(file_path)

    except Exception as e:
        print(f"Reading metadata caused an error: {e}")
        return

    if audio is None:
        print(f"Failed to load file: {file_path}")
        return

    max_len = len('tracknumber')
    for key in audio:
        addstr = (max_len-len(key)) * " "
        print(f"{key}:{addstr} {audio[key]}")


def print_appendable_metadata_single(file_path: str) -> None:
    try:
        if file_path.endswith(".mp3"):
            audio = EasyID3(file_path)
        elif file_path.endswith(".flac"):
            audio = FLAC(file_path)

    except Exception as e:
        print(f"Reading metadata caused an error: {e}")
        return

    if audio is None:
        print(f"Failed to load file: {file_path}")
        return

    specific_md = ['album', 'title', 'artist', 'tracknumber', 'date']
    max_len = len('tracknumber')
    for key in specific_md:
        addstr = (max_len-len(key)) * " "
        if key in audio:
            print(f"{key}:{addstr} {audio[key]}")
        else:
            print(f"{key}:{addstr} Unavailable")


def print_specific_metadata_single(file_path: str, md_name: str) -> None:
    try:
        if file_path.endswith(".mp3"):
            audio = EasyID3(file_path)
        elif file_path.endswith(".flac"):
            audio = FLAC(file_path)

    except Exception as e:
        print(f"Reading metadata caused an error: {e}")
        return

    if audio is None:
        print(f"Failed to load file: {file_path}")
        return

    if md_name in audio:
        print(f"{md_name}: {audio[md_name]}")
    else:
        print(f"{md_name}: Unavailable")
