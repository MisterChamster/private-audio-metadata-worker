from pathlib import Path

import src.removal.remove_single_tools as removers



def remove_all_md_dir(dir_path: Path) -> None:
    for file_path in dir_path.iterdir():
        removers.remove_all_md_file(file_path)
