from pathlib import Path

import src.askers.askers_utils      as ask_utils
import src.askers.askers_main_menus as ask_main
import src.askers.askers_removal    as ask_removal
import src.md_printers.print_file_tools  as printers
import src.appending.append_single_tools as appenders
import src.removal.remove_single_tools   as removers



def append_loop(file_path: Path) -> bool:
    exit_flags = {
        "return": False,
        "exit": True}

    while True:
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


def removal_loop(file_path: Path) -> bool:
    exit_flags = {
        "return": False,
        "exit": True}

    while True:
        removal_type = ask_removal.ask_removal_loop()
        print("\n")

        exit_flags = {"return": False,
                      "exit": True}
        if removal_type in exit_flags:
            return exit_flags[removal_type]

        if removal_type == "all":
            removers.remove_all_md(file_path)

        elif removal_type == "appendable":
            print("Work in progress")

        elif removal_type == "specific":
            print("Work in progress")


def file_loop(file_path: Path) -> bool:
    while True:
        asker = ask_main.ask_main_file_action(file_path)
        print()
        if asker == "print_all":
            printers.print_all_metadata_file(file_path)
            print("\n")

        elif asker == "print_appendable":
            printers.print_appendable_metadata_file(file_path)
            print("\n")

        elif asker == "append":
            exit_flag = append_loop(file_path)
            if exit_flag == True:
                return True

        elif asker == "remove":
            exit_flag = removal_loop(file_path)
            if exit_flag == True:
                return True

        else:
            exit_flags = {
                "change_path": False,
                "exit": True}

            if asker in exit_flags:
                return exit_flags[asker]
