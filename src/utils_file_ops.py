from pathlib import Path
from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC
from mutagen.oggvorbis import OggVorbis



def get_audios_from_dir(
    dir_path: Path,
    sort_it: bool = True
) -> list[Path]:
    valid_exts = (".mp3", ".flac", ".ogg")
    audios_in_dir = []
    for node in dir_path.iterdir():
        if (node.is_file() and
            node.suffix in valid_exts and
            not node.name.startswith(".")):
            audios_in_dir.append(node)

    if sort_it:
        audios_in_dir.sort()

    return audios_in_dir


def get_dirs_from_dir(
    dir_path: Path,
    sort_it: bool = True
) -> list[Path]:
    dirs_list = [node
                 for node in dir_path.iterdir()
                 if node.is_dir()]
    if sort_it:
        dirs_list.sort()

    return dirs_list


def is_audio_in_dir(dir_path: Path) -> bool:
    valid_exts = (".mp3", ".flac", ".ogg")
    for node in dir_path.iterdir():
        if (node.is_file() and
            node.suffix in valid_exts and
            not node.name.startswith(".")):
            return True
    return False


def get_audio(file_path: Path) -> FLAC | OggVorbis | EasyID3:
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

    return audio
