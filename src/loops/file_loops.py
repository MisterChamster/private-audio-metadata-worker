from src.askers.file_askers import (ask_main_file_action,
                                    ask_append_loop)
from src.printing.print_single_universal import (print_all_metadata_single,
                                                 print_appendable_metadata_single)



def append_loop(file_path: str):
    while True:
        asker = ask_append_loop()
        return None


def file_loop(file_path: str):
    while True:
        asker = ask_main_file_action(file_path)
        if asker == "print_all":
            print_all_metadata_single(file_path)
            print()

        elif asker == "print_appendable":
            print_appendable_metadata_single(file_path)
            print()

        elif asker == "append":
            outer = append_loop(file_path)
            if outer == None:
                return None

        elif asker == "change_path":
            return asker

        elif asker == None:
            return None
