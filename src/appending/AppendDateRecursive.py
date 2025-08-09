import os



class AppendDateRecursive:
    def _recurrer(_self, dir_path: str):
        return

    def append_date_dir_recur(self, dir_path: str):
        og_path = os.getcwd()
        self._recurrer(dir_path)
        os.chdir(og_path)
