from src.printing.print_dir_universal import (print_all_metadata_dir,
                                              print_appendable_metadata_dir,
                                              print_specific_metadata_dir)
import os



# Okay, maybe it didn't have to be made with a class,
# but it's good to practise nonetheless
class PrintDirRecursive:
    def __init__(self, md_name: str = None):
        self.md_name = md_name



    def recurrer_all(dir_path: str):
        os.chdir(dir_path)
        print_all_metadata_dir(dir_path)
        os.chdir("..")


    def recurrer_appendable(dir_path: str):
        os.chdir(dir_path)
        print_appendable_metadata_dir(dir_path)
        os.chdir("..")


    def recurrer_specific(self, dir_path: str):
        os.chdir(dir_path)
        print_specific_metadata_dir(dir_path, self.md_name)
        os.chdir("..")


    def print_all_metadata_dir_recur(self, dir_path) -> None:
        og_path = os.getcwd()
        self.recurrer_all(dir_path)
        os.chdir(og_path)


    def print_appendable_metadata_dir_recur(self, dir_path) -> None:
        og_path = os.getcwd()
        self.recurrer_appendable(dir_path)
        os.chdir(og_path)


    def print_specific_metadata_dir_recur(self, dir_path, md_name) -> None:
        og_path = os.getcwd()
        self.md_name = md_name
        self.recurrer_specific(dir_path)
        os.chdir(og_path)
