import os
from pathlib import Path
from src.appending.append_dir_universal import append_title_dir
from src.file_ops.utils import (get_dirs_from_dir,
                                is_audio_in_dir)



class AppendTitleRecursive:
    def _recurrer(self, dir_path: str):
        return

    def append_title_dir_recur(self, dir_path: str):
        og_path = os.getcwd()
        self._recurrer(dir_path)
        os.chdir(og_path)
