from src.askers.dir_askers import ask_main_dir_action
from os import chdir



def directory_loop(dir_path: str):
    chdir(dir_path)
    while True:
        print(f"Directory path: {dir_path}")
        asker = ask_main_dir_action(dir_path)
        if asker == "print":
            pass
        elif asker == "append":
            pass
        elif asker == "change_dir":
            pass
        elif asker == None:
            return None

        # For testing
        return None
