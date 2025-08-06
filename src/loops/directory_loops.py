from src.askers.dir_askers import (ask_main_dir_action,
                                   ask_print_loop,
                                   ask_append_loop)
from src.printing.print_dir_mp3 import (print_all_mp3,
                                        print_appendable_mp3,
                                        print_specific_mp3)
from os import chdir



def print_loop(dir_path: str):
    while True:
        asker = ask_print_loop()
        if asker == "print_all":
            pass
        elif asker == "print_all_recursive":
            pass
        elif asker == "print_appendable":
            pass
        elif asker == "print_appendable_recursive":
            pass
        elif asker == "print_specific":
            pass
        elif asker == "print_specific_recursive":
            pass
        elif asker == None:
            return None


def append_loop(dir_path: str):
    while True:
        asker = ask_append_loop()
        return None


def directory_loop(dir_path: str):
    chdir(dir_path)
    while True:
        asker = ask_main_dir_action(dir_path)
        if asker == "print":
            outer = print_loop(dir_path)
            if outer == None:
                return None

        elif asker == "append":
            outer = append_loop(dir_path)
            if outer == None:
                return None

        elif asker == "change_path":
            return asker

        elif asker == None:
            return None
