from pathlib import Path

import src.utils_file_ops as utils_file
import src.appending.append_dir_tools as append_dir



class AppendRecurDir:
    def __init__(self, md_name: str = None, md_text: str = None):
        self.md_name = md_name
        self.md_text = md_text


    def __recurrer(self, dir_path: Path) -> None:
        print(f"Directory name: {dir_path.name}")
        print()
        append_dir.append_metadata_dir(dir_path, self.md_name, self.md_text)

        dirs_list = utils_file.get_dirs_from_dir(dir_path)
        for dir_name in dirs_list:
            full_path = dir_path / dir_name
            self.__recurrer(full_path)


    def append_metadata_dir_recur(
        self,
        dir_path: Path,
        md_name: str,
        md_text: str
    ) -> None:
        self.md_name = md_name
        self.md_text = md_text
        self.__recurrer(dir_path)
