from src.askers.file_askers import ask_main_file_action
from src.askers.utils_askers import (ask_specific_metadata,
                                     ask_metadata_text)
from src.printing.print_single_universal import (print_all_metadata_single,
                                                 print_appendable_metadata_single)


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
            md_type = ask_specific_metadata()
            print()
            if md_type in ["return", None]:
                return md_type
            else:
                md_text = ask_metadata_text()
                print()

        elif asker == "change_path":
            return asker

        elif asker == None:
            return None
