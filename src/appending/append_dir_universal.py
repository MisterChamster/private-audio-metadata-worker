from src.file_ops.utils import get_audios_from_dir
from pathlib import Path
from src.appending.append_single_universal import append_metadata_file_universal



def append_metadata_dir(dir_path: str, md_type: str, md_text: str):
    files_list = get_audios_from_dir(dir_path)
    for filename in files_list:
        print(filename)
        file_path = str(Path(dir_path) / filename)
        append_metadata_file_universal(file_path, md_type, md_text)
    print()


def append_tracknum_dir(dir_path: str):
    files_list = get_audios_from_dir(dir_path)
    #write more stuff here
