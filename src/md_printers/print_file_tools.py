from pathlib import Path
from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC
from mutagen.oggvorbis import OggVorbis

import src.utils_file_ops as file_ops



def print_all_metadata_file(file_path: Path) -> None:
    audio = file_ops(file_path)

    max_len = len('tracknumber')
    for key in audio:
        addstr = (max_len-len(key)) * " "
        print(f"{key}:{addstr} '{audio[key][0]}'")


def print_appendable_metadata_file(file_path: Path) -> None:
    audio = file_ops(file_path)

    specific_md = ['album', 'title', 'artist', 'tracknumber', 'date']
    max_len = len('tracknumber')
    for key in specific_md:
        addstr = (max_len-len(key)) * " "
        if key in audio:
            print(f"{key}:{addstr} '{audio[key][0]}'")
        else:
            print(f"{key}:{addstr} Unavailable")


def print_specific_metadata_file(file_path: Path, md_name: str) -> None:
    audio = file_ops(file_path)

    if md_name in audio:
        print(f"{md_name}: '{audio[md_name][0]}'")
    else:
        print(f"{md_name}: Unavailable")
