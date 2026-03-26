from pathlib import Path

import src.md_printers.print_dir_tools as printdir
import src.utils_file_ops as utils_file



# Okay, maybe it didn't have to be made with a class,
# but it's good to practise nonetheless
class PrintDirRecursive:
    def __init__(self, md_name: str = None):
        self.md_name = md_name


    # =================== PRINT ALL ===================
    def __recurrer_print_all(
            self, dir_path: Path) -> None:
        print(f"Directory name: {dir_path.name}")
        print()
        printdir.print_all_metadata_dir(dir_path)

        dirs_list = utils_file.get_dirs_from_dir(dir_path, sort_it=True)
        for dir_name in dirs_list:
            full_path = dir_path / dir_name
            self.__recurrer_print_all(full_path)


    def print_all_metadata_dir_recur(
            self, dir_path: Path) -> None:
        self.__recurrer_print_all(dir_path)


    # ================ PRINT APPENDABLE ================
    def __recurrer_print_appendable(
            self, dir_path: Path) -> None:
        print(f"Directory name: {dir_path.name}")
        print()
        printdir.print_appendable_metadata_dir(dir_path)

        dirs_list = utils_file.get_dirs_from_dir(dir_path, sort_it=True)
        for dir_name in dirs_list:
            full_path = dir_path / dir_name
            self.__recurrer_print_appendable(full_path)


    def print_appendable_metadata_dir_recur(
            self, dir_path: Path) -> None:
        self.__recurrer_print_appendable(dir_path)


    # ================= PRINT SPECIFIC =================
    def __recurrer_print_specific(
            self, dir_path: Path) -> None:
        print(f"Directory name: {dir_path.name}")
        print()
        printdir.print_specific_metadata_dir(
            dir_path, self.md_name)

        dirs_list = utils_file.get_dirs_from_dir(dir_path, sort_it=True)
        for dir_name in dirs_list:
            full_path = dir_path / dir_name
            self.__recurrer_print_specific(full_path)


    def print_specific_metadata_dir_recur(
            self, dir_path: Path, md_name: str) -> None:
        self.md_name = md_name
        self.__recurrer_print_specific(dir_path)
