from pathlib import Path

import src.utils_file_ops as utils_file
import src.removal.remove_dir_tools as remove_dir

#   Appending recurrers liftoff responsibility

class RemovalRecurrers:
    md_to_del: str = ""

# ================ Recurrers setups ================
    def remove_all_dir_recur(self, dir_path: Path) -> None:
        self.__recurrer_remove_all(dir_path)


    def remove_appendable_dir_recur(self, dir_path: Path) -> None:
        self.__recurrer_remove_appendable(dir_path)


    def remove_specific_dir_recur(
            self, dir_path: Path, md_to_del: str) -> None:
        self.md_to_del = md_to_del
        self.__recurrer_remove_specific(dir_path)
        self.md_to_del = ""


# ================ Recurrers setups ================
    def __recurrer_remove_all(self, dir_path: Path) -> None:
        print(f"Directory name: {dir_path.name}")
        remove_dir.remove_all_md_dir(dir_path)

        dirs_list = utils_file.get_dirs_from_dir(dir_path, sort_it=True)
        for single_dir in dirs_list:
            self.__recurrer_remove_all(single_dir)


    def __recurrer_remove_appendable(self, dir_path: Path) -> None:
        print(f"Directory name: {dir_path.name}")
        remove_dir.remove_appendable_md_file(dir_path)

        dirs_list = utils_file.get_dirs_from_dir(dir_path, sort_it=True)
        for single_dir in dirs_list:
            self.__recurrer_remove_appendable(single_dir)


    def __recurrer_remove_specific(self, dir_path: Path) -> None:
        print(f"Directory name: {dir_path.name}")
        remove_dir.remove_specific_md_file(dir_path, self.md_to_del)

        dirs_list = utils_file.get_dirs_from_dir(dir_path, sort_it=True)
        for single_dir in dirs_list:
            self.__recurrer_remove_specific(single_dir)
