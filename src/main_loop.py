from os import chdir
from src.askers import ask_path_filedialog



def main_loop():
    print()
    dir_main = ask_path_filedialog("d", "Choose audio directory")
    if dir_main == "":
        return
    chdir(dir_main)

    while True:
        print()
        action = None
        return
