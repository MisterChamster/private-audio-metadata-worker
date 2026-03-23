from pathlib import Path

import src.utils_file_ops as utils_file
import src.md_printers.print_file_tools as prints



def print_all_metadata_dir(dir_path: Path) -> None:
    files_list = utils_file.get_audios_from_dir(dir_path)
    # TEMPPPPPPP
    dir_path = str(dir_path)
    files_list = [str(a.name) for a in files_list]
    for filename in files_list:
        print(filename)
        file_path = str(Path(dir_path) / filename)
        prints.print_all_metadata_file(file_path)
        print()


def print_appendable_metadata_dir(dir_path: str) -> None:
    # TEMPPPPPPP
    files_list = utils_file.get_audios_from_dir(Path(dir_path))
    files_list = [str(a.name) for a in files_list]
    for filename in files_list:
        print(filename)
        file_path = str(Path(dir_path) / filename)
        prints.print_appendable_metadata_file(file_path)
        print()


def print_specific_metadata_dir(dir_path: str, md_name: str) -> None:
    # TEMPPPPPPP
    files_list = utils_file.get_audios_from_dir(Path(dir_path))
    files_list = [str(a.name) for a in files_list]
    for filename in files_list:
        print(filename)
        file_path = str(Path(dir_path) / filename)
        prints.print_specific_metadata_file(file_path, md_name)
        print()


def print_audiofiles_in_dir(dir_path: str, sort_it: bool = True) -> None:
    # TEMPPPPPPP
    audios_list = utils_file.get_audios_from_dir(Path(dir_path), sort_it)
    audios_list = [str(a.name) for a in audios_list]

    for filename in audios_list:
        print(filename)
