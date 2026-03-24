from pathlib import Path

import src.utils_file_ops as utils_file
import src.md_printers.print_file_tools as prints



def print_all_metadata_dir(
        dir_path: Path) -> None:
    files_paths = utils_file.get_audios_from_dir(dir_path)
    for file_path in files_paths:
        print(file_path.name)
        prints.print_all_metadata_file(file_path)
        print()


def print_appendable_metadata_dir(
        dir_path: Path) -> None:
    files_paths = utils_file.get_audios_from_dir(dir_path)
    for file_path in files_paths:
        print(file_path.name)
        file_path = dir_path / file_path
        prints.print_appendable_metadata_file(file_path)
        print()


def print_specific_metadata_dir(
        dir_path: Path, md_name: str) -> None:
    files_paths = utils_file.get_audios_from_dir(dir_path)
    for file_path in files_paths:
        print(file_path.name)
        prints.print_specific_metadata_file(file_path, md_name)
        print()


def print_audiofiles_in_dir(
    dir_path: Path, sort_it: bool = True) -> None:
    audios_list = utils_file.get_audios_from_dir(dir_path, sort_it)

    for file_path in audios_list:
        print(file_path.name)
