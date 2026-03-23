from pathlib import Path
from os import chdir

import src.md_printers.print_dir_tools as printdir
import src.utils_file_ops as utils_file



# Okay, maybe it didn't have to be made with a class,
# but it's good to practise nonetheless
class PrintDirRecursive:
    def __init__(self, md_name: str = None):
        self.md_name = md_name


    # =================== PRINT ALL ===================
    def __recurrer_all(
            self, dir_path: Path) -> None:
        chdir(dir_path)
        print(f"Directory name: {dir_path.name}")
        print()
        printdir.print_all_metadata_dir(dir_path)

        dirs_list = utils_file.get_dirs_from_dir(dir_path)
        for dir_name in dirs_list:
            full_path = dir_path / dir_name
            self.__recurrer_all(full_path)
        chdir("..")


    def print_all_metadata_dir_recur(
            self, dir_path: Path) -> None:
        og_path = Path.cwd()
        self.__recurrer_all(dir_path)
        chdir(og_path)


    # ================ PRINT APPENDABLE ================
    def __recurrer_appendable(
            self, dir_path: Path) -> None:
        chdir(dir_path)
        print(f"Directory name: {dir_path.name}")
        print()
        printdir.print_appendable_metadata_dir(dir_path)

        dirs_list = utils_file.get_dirs_from_dir(dir_path)
        for dir_name in dirs_list:
            full_path = dir_path / dir_name
            self.__recurrer_appendable(full_path)
        chdir("..")


    def print_appendable_metadata_dir_recur(
            self, dir_path: Path) -> None:
        og_path = Path.cwd()
        self.__recurrer_appendable(dir_path)
        chdir(og_path)


    # ================= PRINT SPECIFIC =================
    def __recurrer_specific(
            self, dir_path: Path) -> None:
        chdir(dir_path)
        print(f"Directory name: {dir_path.name}")
        print()
        printdir.print_specific_metadata_dir(
            dir_path, self.md_name)

        dirs_list = utils_file.get_dirs_from_dir(dir_path)
        for dir_name in dirs_list:
            full_path = dir_path / dir_name
            self.__recurrer_specific(full_path)
        chdir("..")


    def print_specific_metadata_dir_recur(
            self, dir_path: Path, md_name: str) -> None:
        self.md_name = md_name
        og_path = Path.cwd()
        self.__recurrer_specific(dir_path)
        chdir(og_path)
