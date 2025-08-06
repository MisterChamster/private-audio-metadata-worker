from src.file_ops.utils import get_audios_from_cwd
from src.printing.print_single_mp3 import (print_all_metadata_mp3,
                                           print_appendable_metadata_mp3,
                                           print_specific_metadata_mp3)
from src.printing.print_single_flac import (print_all_metadata_flac,
                                            print_appendable_metadata_flac,
                                            print_specific_metadata_flac)
from pathlib import Path



def print_all_metadata_dir(dir_path: str) -> None:
    files_list = get_audios_from_cwd(dir_path)
    for filename in files_list:
        print(filename)
        file_path = Path(dir_path) / filename
        if filename.endswith(".mp3"):
            print_all_metadata_mp3(file_path)
        elif filename.endswith(".flac"):
            print_all_metadata_flac(file_path)
        print()


def print_appendable_metadata_dir(dir_path: str) -> None:
    files_list = get_audios_from_cwd(dir_path)
    for filename in files_list:
        file_path = Path(dir_path) / filename
        print_appendable_metadata_mp3(file_path)
        print()


def print_specific_metadata_dir(dir_path: str, md_name: str) -> None:
    files_list = get_audios_from_cwd(dir_path)
    for filename in files_list:
        file_path = Path(dir_path) / filename
        print_specific_metadata_mp3(file_path, md_name)
        print()
