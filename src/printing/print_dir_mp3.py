from src.file_ops.utils import get_audios_from_cwd



def print_all_mp3(dir_path: str) -> None:
    files_list = get_audios_from_cwd(dir_path)
    for filename in files_list:
        print(filename)


def print_appendable_mp3(dir_path: str) -> None:
    return


def print_specific_mp3(dir_path: str, md_name: str) -> None:
    return
