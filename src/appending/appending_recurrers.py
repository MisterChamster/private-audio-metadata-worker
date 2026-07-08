from pathlib import Path

import src.utils_file_ops as utils_file
import src.askers.askers_appending as ask_append
import src.appending.append_dir_tools as append_dir




class AppendingRecurrers:
    del_until: str      = ""
    md_name:   str|None = None
    md_text:   str|None = None


# ================ Recurrers setups ================
    def append_tracknum_dir_recur(self, dir_path: Path) -> None:
        self.__recurrer_append_tracknum(dir_path)


    def append_title_dir_recur(self, dir_path: Path) -> None:
        self.del_until = ask_append.ask_del_until()
        print("\n")
        self.__recurrer_append_title(dir_path)


    def append_metadata_dir_recur(
        self, dir_path: Path, md_name: str, md_text: str) -> None:
        self.md_name = md_name
        self.md_text = md_text
        self.__recurrer_append_metadata(dir_path)


    def append_album_dir_recur(self, dir_path: Path) -> None:
        self.del_until = ask_append.ask_del_until()
        print("\n")
        self.__recurrer_append_album(dir_path)


    def append_date_dir_recur(self, dir_path: Path) -> None:
        self.__recurrer_append_date(dir_path)


# ================ Recurrers setups ================
    def __recurrer_append_album(self, dir_path: Path) -> None:
        print(f"Directory name: {dir_path.name}")
        print()
        if utils_file.is_audio_in_dir(dir_path):
            append_dir.append_album_dir(dir_path, self.del_until)
            print("\n\n")

        dirs_list = utils_file.get_dirs_from_dir(dir_path, sort_it=True)
        for dir_name in dirs_list:
            full_path = dir_path / dir_name
            self.__recurrer_append_album(full_path)


    def __recurrer_append_date(self, dir_path: Path) -> None:
        if utils_file.is_audio_in_dir(dir_path):
            append_dir.append_date_dir(dir_path)
            print()

        dirs_list = utils_file.get_dirs_from_dir(dir_path, sort_it=True)
        for dir_name in dirs_list:
            full_path = dir_path / dir_name
            self.__recurrer_append_date(full_path)


    def __recurrer_append_metadata(self, dir_path: Path) -> None:
        print(f"Directory name: {dir_path.name}")
        print()
        append_dir.append_metadata_dir(dir_path, self.md_name, self.md_text)

        dirs_list = utils_file.get_dirs_from_dir(dir_path, sort_it=True)
        for dir_name in dirs_list:
            full_path = dir_path / dir_name
            self.__recurrer_append_metadata(full_path)


    def __recurrer_append_title(self, dir_path: Path) -> None:
        print(f"Directory name: {dir_path.name}")
        print()
        if utils_file.is_audio_in_dir(dir_path):
            append_dir.append_title_dir(dir_path, self.del_until)

        dirs_list = utils_file.get_dirs_from_dir(dir_path, sort_it=True)
        for dir_name in dirs_list:
            full_path = dir_path / dir_name
            self.__recurrer_append_title(full_path)


    def __recurrer_append_tracknum(self, dir_path: Path) -> None:
        print(f"Directory name: {dir_path.name}")
        print()
        if utils_file.is_audio_in_dir(dir_path):
            append_dir.append_tracknum_dir(dir_path)
            print("\n")

        dirs_list = utils_file.get_dirs_from_dir(dir_path, sort_it=True)
        for dir_name in dirs_list:
            full_path = dir_path / dir_name
            self.__recurrer_append_tracknum(full_path)
