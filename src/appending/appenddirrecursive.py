from src.appending.append_dir_universal import append_metadata_dir
from src.file_ops.utils import get_dirs_from_dir
import os
from pathlib import Path



class AppendDirRecursive:
    def __init__(self, md_name: str = None, md_text: str = None):
        self.md_name = md_name
        self.md_text = md_text


    def _recurrer(self, dir_path: str):
        os.chdir(dir_path)
        print(f"Directory name: {os.path.basename(dir_path)}")
        print()
        append_metadata_dir(dir_path, self.md_name, self.md_text)

        dirs_list = get_dirs_from_dir(dir_path)
        for dir_name in dirs_list:
            full_path = str(Path(dir_path) / dir_name)
            self._recurrer(full_path)
        os.chdir("..")


    def append_metadata_dir_recur(self, dir_path: str, md_name: str, md_text: str):
        self.md_name = md_name
        self.md_text = md_text
        og_path = os.getcwd()
        self._recurrer(dir_path)
        os.chdir(og_path)
