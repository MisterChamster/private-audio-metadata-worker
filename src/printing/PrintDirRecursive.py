class PrintDirRecursive:
    def __init__(self, dir_path: str, md_name: str):
        self.dir_path = dir_path
        self.md_name = md_name



    def recurrer_all():
        return


    def recurrer_appendable():
        return


    def recurrer_specific():
        return


    def print_all_metadata_dir_recur(self, dir_path) -> None:
        self.dir_path = dir_path
        self.recurrer_all()


    def print_appendable_metadata_dir_recur(self, dir_path) -> None:
        self.dir_path = dir_path
        self.recurrer_appendable()


    def print_specific_metadata_dir_recur(self, dir_path, md_name) -> None:
        self.dir_path = dir_path
        self.md_name = md_name
        self.recurrer_specific()
