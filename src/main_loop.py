from os import chdir
from src.askers.main_asker import ask_path_filedialog, ask_main_action



def main_loop():
    print()
    dir_main = ask_path_filedialog("d", "Choose audio directory")
    if dir_main == "":
        return
    chdir(dir_main)

    while True:
        print()
        print(f"Current directory: {dir_main}")
        action = ask_main_action()
        if action == None:
            return
        elif action == "print":
            pass
        elif action == "append":
            pass
        elif action == "change":
            dir_main = ask_path_filedialog("d", "Choose audio directory")
            if dir_main == "":
                return
            chdir(dir_main)
