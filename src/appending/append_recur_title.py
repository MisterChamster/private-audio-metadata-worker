from pathlib import Path
from os import chdir

import src.appending.append_dir_tools as append_dir
import src.utils_file_ops as utils_file
import src.askers.askers_appending as ask_append



class AppendRecurTitle:
    def __init__(self, del_until: str = ""):
        self.del_until = del_until

    def __recurrer(self, dir_path: Path) -> None:
        chdir(dir_path)
        print(f"Directory name: {dir_path.name}")
        print()
        if utils_file.is_audio_in_dir(dir_path):
            append_dir.append_title_dir(dir_path, self.del_until)

        dirs_list = utils_file.get_dirs_from_dir(dir_path)
        for dir_name in dirs_list:
            full_path = dir_path / dir_name
            self.__recurrer(full_path)
        chdir("..")

    def append_title_dir_recur(self, dir_path: Path) -> None:
        self.del_until = ask_append.ask_del_until()
        print("\n")
        og_path = Path.cwd()
        self.__recurrer(dir_path)
        chdir(og_path)
