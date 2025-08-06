from src.printing.print_single_mp3 import (print_all_mp3,
                                           print_appendable_mp3,
                                           print_specific_mp3)
from src.printing.print_single_flac import (print_all_flac,
                                            print_appendable_flac,
                                            print_specific_flac)




def print_all(file_path: str) -> None:
    if file_path.endswith(".mp3"):
        print_all_mp3(file_path)
    elif file_path.endswith(".flac"):
        print_all_flac(file_path)


def print_appendable(file_path: str) -> None:
    if file_path.endswith(".mp3"):
        print_appendable_mp3(file_path)
    elif file_path.endswith(".flac"):
        print_appendable_flac(file_path)


def print_specific(file_path: str, md_name: str) -> None:
    if file_path.endswith(".mp3"):
        print_specific_mp3(file_path, md_name)
    elif file_path.endswith(".flac"):
        print_specific_flac(file_path, md_name)
