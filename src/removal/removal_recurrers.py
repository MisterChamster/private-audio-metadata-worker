from pathlib import Path

import src.utils_file_ops as utils_file
import src.removal.remove_dir_tools as remove_dir

#   Appending recurrers liftoff responsibility

class RemovalRecurrers:
# ================ Recurrers setups ================
    def remove_all_dir_recur(self, dir_path: Path) -> None:
        self.__recurrer_remove_all(dir_path)


    def remove_appendable_dir_recur(self, dir_path: Path) -> None:
        self.__recurrer_remove_appendable(dir_path)


    def remove_specific_dir_recur(self, dir_path: Path) -> None:
        pass


# ================ Recurrers setups ================
    def __recurrer_remove_all(self, dir_path: Path) -> None:
        print(f"Directory name: {dir_path.name}\n")
        remove_dir.remove_all_md_dir(dir_path)
        pass

    def __recurrer_remove_appendable(self, dir_path: Path) -> None:
        print(f"Directory name: {dir_path.name}\n")
        remove_dir.remove_appendable_md_file(dir_path)
        pass

    def __recurrer_remove_specific(self, dir_path: Path) -> None:
        pass
