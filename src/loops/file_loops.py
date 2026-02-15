import os

import src.askers.askers_main_menus as ask_main
import src.askers.askers_utils      as ask_utils
import src.md_printers.print_file_tools as printers
from src.appending.append_single_tools import append_metadata_file_universal


def file_loop(file_path: str) -> str | None:
    while True:
        asker = ask_main.ask_main_file_action(file_path)
        print("\n")
        if asker == "print_all":
            printers.print_all_metadata_file(file_path)
            print()

        elif asker == "print_appendable":
            printers.print_appendable_metadata_file(file_path)
            print()

        elif asker == "append":
            md_type = ask_utils.ask_specific_metadata()
            print("\n")
            if md_type in ["return", None]:
                return md_type
            else:
                md_text = ask_utils.ask_metadata_text()
                print("/n")
                try:
                    append_metadata_file_universal(file_path, md_type, md_text)
                    print(f"Metadata successfully appended to: {os.path.basename(file_path)}")
                except Exception as e:
                    print(f"Appending metadata failed. Error: {e}")
                finally:
                    print("\n\n")

        elif asker == "change_path":
            return asker

        elif not asker:
            return
