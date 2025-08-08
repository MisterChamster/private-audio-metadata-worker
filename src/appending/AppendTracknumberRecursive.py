import os



class AppendTracknumberRecursive:
    def _recurrer(self, dir_path: str):
        return

    def append_metadata_dir_recur(self, dir_path: str):
        og_path = os.getcwd()
        self._recurrer(dir_path)
        os.chdir(og_path)
