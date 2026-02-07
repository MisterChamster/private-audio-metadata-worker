import os
from pathlib import Path
from src.appending.append_dir_universal import append_title_dir
import src.utils_file_ops as utils_file
from src.askers.askers_appending import ask_del_until



class AppendTitleRecursive:
    def __init__(self, del_until: str = ""):
        self.del_until = del_until

    def __recurrer(self, dir_path: str):
        os.chdir(dir_path)
        print(f"Directory name: {os.path.basename(dir_path)}")
        print()
        if utils_file.is_audio_in_dir(dir_path):
            append_title_dir(dir_path, self.del_until)

        dirs_list = utils_file.get_dirs_from_dir(dir_path)
        for dir_name in dirs_list:
            full_path = str(Path(dir_path) / dir_name)
            self.__recurrer(full_path)
        os.chdir("..")

    def append_title_dir_recur(self, dir_path: str):
        self.del_until = ask_del_until()
        print()
        og_path = os.getcwd()
        self.__recurrer(dir_path)
        os.chdir(og_path)
