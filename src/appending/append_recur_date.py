from pathlib import Path

import src.utils_file_ops as utils_file
import src.appending.append_dir_tools as append_dir



class AppendRecurDate:
    def __recurrer(self, dir_path: Path) -> None:
        # print(f"Directory name: {dir_path.name}")
        # print()
        if utils_file.is_audio_in_dir(dir_path):
            append_dir.append_date_dir(dir_path)
            print()

        dirs_list = utils_file.get_dirs_from_dir(dir_path)
        for dir_name in dirs_list:
            full_path = dir_path / dir_name
            self.__recurrer(full_path)

    # Don't mind me!
    def append_date_dir_recur(self, dir_path: Path) -> None:
        self.__recurrer(dir_path)
