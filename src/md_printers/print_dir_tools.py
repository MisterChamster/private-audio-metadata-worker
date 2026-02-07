from pathlib import Path

import src.utils_file_ops as utils_file
from src.md_printers.print_file_tools import (print_all_metadata_file,
                                                 print_appendable_metadata_file,
                                                 print_specific_metadata_file)



def print_all_metadata_dir(dir_path: str) -> None:
    files_list = utils_file.get_audios_from_dir(dir_path)
    for filename in files_list:
        print(filename)
        file_path = str(Path(dir_path) / filename)
        print_all_metadata_file(file_path)
        print()


def print_appendable_metadata_dir(dir_path: str) -> None:
    files_list = utils_file.get_audios_from_dir(dir_path)
    for filename in files_list:
        print(filename)
        file_path = str(Path(dir_path) / filename)
        print_appendable_metadata_file(file_path)
        print()


def print_specific_metadata_dir(dir_path: str, md_name: str) -> None:
    files_list = utils_file.get_audios_from_dir(dir_path)
    for filename in files_list:
        print(filename)
        file_path = str(Path(dir_path) / filename)
        print_specific_metadata_file(file_path, md_name)
        print()


def print_audiofiles_in_dir(dir_path: str, sort_it: bool = True) -> None:
    audios_list = utils_file.get_audios_from_dir(dir_path, sort_it)

    for filename in audios_list:
        print(filename)
