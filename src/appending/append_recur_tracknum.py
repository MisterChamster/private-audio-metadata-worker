import os
from pathlib import Path

import src.appending.append_dir_tools as append_dir
import src.utils_file_ops as utils_file



class AppendRecurTracknum:
    def __recurrer(self, dir_path: Path) -> None:
        os.chdir(dir_path)
        print(f"Directory name: {dir_path.name}")
        print()
        if utils_file.is_audio_in_dir(dir_path):
            append_dir.append_tracknum_dir(dir_path)
            print("\n\n")

        # TEMPPPPPPP
        dirs_list = utils_file.get_dirs_from_dir(str(dir_path))
        for dir_name in dirs_list:
            full_path = str(Path(dir_path) / dir_name)
            self.__recurrer(full_path)
        os.chdir("..")


    def append_tracknum_dir_recur(self, dir_path: Path) -> None:
        og_path = Path.cwd()
        self.__recurrer(dir_path)
        os.chdir(og_path)
