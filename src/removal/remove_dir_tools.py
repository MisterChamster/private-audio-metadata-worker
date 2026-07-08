from pathlib import Path

import src.utils_file_ops as utils_file
import src.removal.remove_single_tools as removers



def remove_all_md_dir(dir_path: Path) -> None:
    files_paths = utils_file.get_audios_from_dir(dir_path)
    for file_path in files_paths:
        removers.remove_all_md_file(file_path)


def remove_appendable_md_file(dir_path: Path) -> None:
    files_paths = utils_file.get_audios_from_dir(dir_path)
    for file_path in files_paths:
        removers.remove_appendable_md_file(file_path)


def remove_specific_md_file(dir_path: Path, md_to_rm: str) -> None:
    files_paths = utils_file.get_audios_from_dir(dir_path)
    for file_path in files_paths:
        removers.remove_specific_md_file(file_path, md_to_rm)
