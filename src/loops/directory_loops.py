from src.askers.dir_askers import ask_main_dir_action
from os import chdir



def directory_loop(dir_path: str):
    chdir(dir_path)
    while True:
        print(f"Directory path: {dir_path}")
        outer = ask_main_dir_action(dir_path)
        if outer == None:
            return None
        return None
