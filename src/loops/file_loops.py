from pathlib import Path

import src.askers.askers_utils      as ask_utils
import src.askers.askers_main_menus as ask_main
import src.md_printers.print_file_tools  as printers
import src.appending.append_single_tools as appenders


def file_loop(file_path: Path) -> bool:
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
            exit_flags = {"return": False, "exit": True}

            if md_type in exit_flags:
                return exit_flags[md_type]

            md_text = ask_utils.ask_metadata_text()
            print("\n")
            try:
                appenders.append_metadata_file_universal(
                    file_path, md_type, md_text)
                print(f"Metadata successfully appended to: {file_path.name}")
            except Exception as e:
                print(f"Appending metadata failed. Error: {e}")
            finally:
                print("\n\n")

        else:
            exit_flags = {
                "change_path": False,
                "exit": True}

            if asker in exit_flags:
                return exit_flags[asker]
