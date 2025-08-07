import os



class AppendDirRecursive:
    def __init__(self, md_name: str = None, md_text: str = None):
        self.md_name = md_name
        self.md_text = md_text


    def _recurrer(self, dir_path: str):
        return


    def append_metadata_dir_recur(self, dir_path: str, md_name: str, md_text: str):
        og_path = os.getcwd()
        self._recurrer(dir_path)
        os.chdir(og_path)
