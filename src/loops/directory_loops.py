from src.askers.dir_askers import (ask_main_dir_action,
                                   ask_print_loop,
                                   ask_append_loop)
from src.printing.print_dir_universal import (print_all_metadata_dir,
                                              print_appendable_metadata_dir,
                                              print_specific_metadata_dir)
from src.printing.PrintDirRecursive import PrintDirRecursive
from src.askers.utils_askers import (ask_specific_metadata,
                                     ask_metadata_text)
from src.appending.append_dir_universal import append_metadata_dir
from os import chdir



def print_loop(dir_path: str):
    while True:
        asker = ask_print_loop()
        print()
        if asker == "print_all":
            print_all_metadata_dir(dir_path)
            print()

        elif asker == "print_all_recursive":
            temp = PrintDirRecursive()
            temp.print_all_metadata_dir_recur(dir_path)
            print()

        elif asker == "print_appendable":
            print_appendable_metadata_dir(dir_path)
            print()

        elif asker == "print_appendable_recursive":
            temp = PrintDirRecursive()
            temp.print_appendable_metadata_dir_recur(dir_path)
            print()

        elif asker == "print_specific":
            md_type = ask_specific_metadata()
            print()
            if md_type == "return" or md_type == None:
                return md_type
            else:
                print_specific_metadata_dir(dir_path, md_type)

        elif asker == "print_specific_recursive":
            md_type = ask_specific_metadata()
            print()
            if md_type == "return" or md_type == None:
                return md_type
            else:
                temp = PrintDirRecursive()
                temp.print_specific_metadata_dir_recur(dir_path, md_type)
                print()

        elif asker == "return":
            return asker

        elif asker == None:
            return None


def append_loop(dir_path: str):
    while True:
        asker = ask_append_loop()
        print()
        if asker == "append_metadata":
            md_type = ask_specific_metadata()
            print()
            if md_type == "return" or md_type == None:
                return md_type
            else:
                md_text = ask_metadata_text()
                print()
                append_metadata_dir(dir_path, md_type, md_text)

        elif asker == "append_metadata_recursive":
            md_type = ask_specific_metadata()
            print()
            if md_type == "return" or md_type == None:
                return md_type
            else:
                md_text = ask_metadata_text()
                print()
                # get back here
                return

        elif asker == "append_tracknumber":
            pass

        elif asker == "append_tracknumber_recursive":
            pass

        elif asker == "return":
            return asker

        elif asker == None:
            return None


def directory_loop(dir_path: str):
    chdir(dir_path)
    while True:
        asker = ask_main_dir_action(dir_path)
        print()
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
