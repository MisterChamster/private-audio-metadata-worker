import os



# Okay, maybe id didn't have to be made with a class,
# but it's a good practise nonetheless
class PrintDirRecursive:
    def __init__(self, md_name: str):
        self.md_name = md_name



    def recurrer_all():
        return


    def recurrer_appendable():
        return


    def recurrer_specific():
        return


    def print_all_metadata_dir_recur(self) -> None:
        og_path = os.getcwd()
        self.recurrer_all()
        os.chdir(og_path)


    def print_appendable_metadata_dir_recur(self) -> None:
        og_path = os.getcwd()
        self.recurrer_appendable()
        os.chdir(og_path)


    def print_specific_metadata_dir_recur(self, md_name) -> None:
        og_path = os.getcwd()
        self.md_name = md_name
        self.recurrer_specific()
        os.chdir(og_path)
