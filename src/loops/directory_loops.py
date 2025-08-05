from src.askers.dir_askers import ask_main_dir_action
from os import chdir



def directory_loop(dir_path: str):
    chdir(dir_path)
    return None
