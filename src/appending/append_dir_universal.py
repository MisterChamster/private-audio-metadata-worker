from src.file_ops.utils import get_audios_from_dir
from pathlib import Path
from src.appending.append_single_universal import append_metadata_file_universal
from src.utils import (get_tracknumber,
                       get_title)
from src.askers.utils_askers import ask_accept



def append_metadata_dir(dir_path: str, md_type: str, md_text: str):
    files_list = get_audios_from_dir(dir_path)
    for filename in files_list:
        print(filename)
        file_path = str(Path(dir_path) / filename)
        append_metadata_file_universal(file_path, md_type, md_text)
    print()


def append_tracknum_dir(dir_path: str):
    files_list = get_audios_from_dir(dir_path)
    tracknums_list = []
    for filename in files_list:
        try:
            tracknums_list.append(get_tracknumber(filename))
        except Exception as e:
            print(f"Getting track from {filename} number caused an error: {e}")
            tracknums_list.append(None)

    for i in range(len(files_list)):
        print(f"Number: {tracknums_list[i]} for track: {files_list[i]}")
    print()

    user_accept = ask_accept()
    print()
    if not user_accept:
        return

    for i in range(len(files_list)):
        if tracknums_list[i] is not None:
            file_path = str(Path(dir_path) / files_list[i])
            append_metadata_file_universal(file_path, "tracknumber", tracknums_list[i])


def append_title_dir(dir_path: str):
    files_list = get_audios_from_dir(dir_path)
    titles_list = []

    for filename in files_list:
        print(get_title(filename))
