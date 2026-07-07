from pathlib import Path

import src.utils_file_ops as utils_file
import src.askers.askers_appending as ask_append
import src.appending.append_dir_tools as append_dir



class AppendRecurTitle:
    del_until: str = ""


    def __recurrer_append_title(self, dir_path: Path) -> None:
        print(f"Directory name: {dir_path.name}")
        print()
        if utils_file.is_audio_in_dir(dir_path):
            append_dir.append_title_dir(dir_path, self.del_until)

        dirs_list = utils_file.get_dirs_from_dir(dir_path, sort_it=True)
        for dir_name in dirs_list:
            full_path = dir_path / dir_name
            self.__recurrer_append_title(full_path)


    def append_title_dir_recur(self, dir_path: Path) -> None:
        self.del_until = ask_append.ask_del_until()
        print("\n")
        self.__recurrer_append_title(dir_path)
