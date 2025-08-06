from src.printing.print_dir_universal import (print_all_metadata_dir,
                                              print_appendable_metadata_dir,
                                              print_specific_metadata_dir)
from src.file_ops.utils import get_dirs_from_dir
import os
from pathlib import Path



# Okay, maybe it didn't have to be made with a class,
# but it's good to practise nonetheless
class PrintDirRecursive:
    def __init__(self, md_name: str = None):
        self.md_name = md_name



    def _recurrer_all(self, dir_path: str):
        os.chdir(dir_path)
        print(f"Directory name: {os.path.basename(dir_path)}")
        print()
        print_all_metadata_dir(dir_path)
        dirs_list = get_dirs_from_dir(dir_path)
        # print(dirs_list)
        for dir_name in dirs_list:
            full_path = Path(dir_path) / dir_name
            self._recurrer_all(full_path)
        os.chdir("..")


    def _recurrer_appendable(self, dir_path: str):
        os.chdir(dir_path)
        print_appendable_metadata_dir(dir_path)
        dirs_list = get_dirs_from_dir(dir_path)
        os.chdir("..")


    def _recurrer_specific(self, dir_path: str):
        os.chdir(dir_path)
        print_specific_metadata_dir(dir_path, self.md_name)
        dirs_list = get_dirs_from_dir(dir_path)
        os.chdir("..")


    def print_all_metadata_dir_recur(self, dir_path) -> None:
        og_path = os.getcwd()
        self._recurrer_all(dir_path)
        os.chdir(og_path)


    def print_appendable_metadata_dir_recur(self, dir_path) -> None:
        og_path = os.getcwd()
        self._recurrer_appendable(dir_path)
        os.chdir(og_path)


    def print_specific_metadata_dir_recur(self, dir_path, md_name) -> None:
        og_path = os.getcwd()
        self.md_name = md_name
        self._recurrer_specific(dir_path)
        os.chdir(og_path)
