from src.file_ops.utils import get_audios_from_cwd
from src.printing.print_single_mp3 import (print_all_metadata_mp3,
                                           print_appendable_metadata_mp3,
                                           print_specific_metadata_mp3)
from pathlib import Path



def print_dir_all_metadata_mp3(dir_path: str) -> None:
    files_list = get_audios_from_cwd(dir_path)
    for filename in files_list:
        file_path = Path(dir_path) / filename
        print_all_metadata_mp3(file_path)
        print()


def print_dir_appendable_metadata_mp3(dir_path: str) -> None:
    return


def print_dir_specific_metadata_mp3(dir_path: str, md_name: str) -> None:
    return
