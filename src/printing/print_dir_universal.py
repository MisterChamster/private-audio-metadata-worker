from src.file_ops.utils_file_ops import get_audios_from_dir
from src.printing.print_single_universal import (print_all_metadata_file,
                                                 print_appendable_metadata_file,
                                                 print_specific_metadata_file)
from pathlib import Path



def print_all_metadata_dir(dir_path: str) -> None:
    files_list = get_audios_from_dir(dir_path)
    for filename in files_list:
        print(filename)
        file_path = str(Path(dir_path) / filename)
        print_all_metadata_file(file_path)
        print()


def print_appendable_metadata_dir(dir_path: str) -> None:
    files_list = get_audios_from_dir(dir_path)
    for filename in files_list:
        print(filename)
        file_path = str(Path(dir_path) / filename)
        print_appendable_metadata_file(file_path)
        print()


def print_specific_metadata_dir(dir_path: str, md_name: str) -> None:
    files_list = get_audios_from_dir(dir_path)
    for filename in files_list:
        print(filename)
        file_path = str(Path(dir_path) / filename)
        print_specific_metadata_file(file_path, md_name)
        print()
