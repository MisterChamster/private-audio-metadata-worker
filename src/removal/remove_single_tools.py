from pathlib import Path

import src.utils_file_ops as file_ops



def remove_all_md_file(file_path: Path) -> None:
    # Safe against mac files ugh
    filename = file_path.name
    if filename.startswith("."):
        return

    audio = file_ops.get_audio(file_path)
    for key in audio.keys():
        audio.pop(key)
    audio.save()


def remove_appendable_md_file(file_path: Path) -> None:
    # Safe against mac files ugh
    filename = file_path.name
    if filename.startswith("."):
        return

    audio = file_ops.get_audio(file_path)
