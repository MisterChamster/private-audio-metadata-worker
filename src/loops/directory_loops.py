from src.askers.dir_askers import (ask_main_dir_action,
                                   ask_print_loop,
                                   ask_append_loop)
from os import chdir



def print_loop():
    while True:
        return None


def append_loop():
    while True:
        return None


def directory_loop(dir_path: str):
    chdir(dir_path)
    while True:
        asker = ask_main_dir_action(dir_path)
        if asker == "print":
            outer = print_loop()
            if outer == None:
                return None

        elif asker == "append":
            outer = append_loop()
            if outer == None:
                return None

        elif asker == "change_path":
            return asker

        elif asker == None:
            return None

        # For testing
        return None
