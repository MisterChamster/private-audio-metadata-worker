import os
from pathlib import Path
import src.utils_file_ops as utils_file
from src.appending.append_dir_universal import append_date_dir



class AppendDateRecursive:
    def __recurrer(self, dir_path: str):
        os.chdir(dir_path)
        # dirname = os.path.basename(dir_path)
        # print(f"Directory name: {dirname}")
        # print()
        if utils_file.is_audio_in_dir(dir_path):
            append_date_dir(dir_path)
            print()

        dirs_list = utils_file.get_dirs_from_dir(dir_path)
        for dir_name in dirs_list:
            full_path = str(Path(dir_path) / dir_name)
            self.__recurrer(full_path)
        os.chdir("..")

    def append_date_dir_recur(self, dir_path: str):
        og_path = os.getcwd()
        self.__recurrer(dir_path)
        os.chdir(og_path)
