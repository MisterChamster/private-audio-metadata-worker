import os
from pathlib import Path



def get_audios_from_dir(
    dir_path: Path,
    sort_it: bool = True
) -> list[Path]:
    valid_exts = ("mp3", "flac")
    audios_in_dir = []
    for node in dir_path.iterdir():
        node_name = node.name
        if (node.suffix in valid_exts and
            not node_name.startswith(".")):
            audios_in_dir.append(node)

    if sort_it:
        audios_in_dir.sort()

    return audios_in_dir


def get_dirs_from_dir(dir_path: str, sort_it: bool = True) -> list[str]:
    og_path = os.getcwd()
    os.chdir(dir_path)
    dirs_list = [node for node in os.listdir() if os.path.isdir(node)]
    if sort_it:
        dirs_list.sort()
    os.chdir(og_path)
    return dirs_list


def is_audio_in_dir(dir_path: str) -> bool:
    valid_exts = ("mp3", "flac")
    for node in os.listdir(dir_path):
        if node.split(".")[-1] in valid_exts and node[0] != ".":
            return True
    return False
