from pathlib import Path
from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC
from mutagen.oggvorbis import OggVorbis



class AudioKeysRecur:
    all_keys: list[str] = []

    def get_audio_keys_dir_recursive(
            self, dir_path: Path, sort_it: bool = True) -> list[str]:
        self.all_keys = []
        self.__recurrer_get_audio_keys(dir_path)

        if sort_it:
            self.all_keys.sort()
        return self.all_keys

    def __recurrer_get_audio_keys(self, dir_path: Path) -> None:
        for file_path in get_audios_from_dir(dir_path):
            audio_keys = get_audio_keys(file_path)
            for key in audio_keys:
                if key not in self.all_keys:
                    self.all_keys.append(key)

        dirs_list = get_dirs_from_dir(dir_path, sort_it=True)
        for single_dir in dirs_list:
            self.__recurrer_get_audio_keys(single_dir)


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


def get_audio_keys(file_path: Path) -> list[str]:
    audios = get_audio(file_path)
    keys = audios.keys()
    return keys


def get_audio_keys_dir(dir_path: Path, sorted: bool = True) -> list[str]:
    all_keys = []

    for file_path in dir_path.iterdir():
        audio_keys = get_audio_keys(file_path)
        for key in audio_keys:
            if key not in all_keys:
                all_keys.append(key)

    if sorted:
        all_keys.sort()

    return all_keys
