from pathlib import Path



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
