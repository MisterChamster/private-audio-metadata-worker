from pathlib import Path

import src.utils_file_ops as file_utils
import src.askers.askers_main_menus as ask_main
import src.askers.askers_appending  as ask_append
import src.askers.askers_removal    as ask_removal
import src.askers.askers_utils      as ask_utils
import src.md_printers.print_dir_tools as print_dir
import src.appending.append_dir_tools  as append_dir
import src.removal.remove_dir_tools    as remove_dir
from src.md_printers.print_dir_recursive import PrintDirRecursive
from src.appending.appending_recurrers   import AppendingRecurrers
from src.removal.removal_recurrers       import RemovalRecurrers



def print_loop(dir_path: Path) -> bool:
    exit_flags = {
        "return": False,
        "exit": True}

    while True:
        asker = ask_main.ask_print_loop()
        print("\n")
        if asker == "print_all":
            print_dir.print_all_metadata_dir(dir_path)
            print()

        elif asker == "print_all_recursive":
            temp = PrintDirRecursive()
            temp.print_all_metadata_dir_recur(dir_path)
            print()

        elif asker == "print_appendable":
            print_dir.print_appendable_metadata_dir(dir_path)
            print()

        elif asker == "print_appendable_recursive":
            temp = PrintDirRecursive()
            temp.print_appendable_metadata_dir_recur(dir_path)
            print()

        elif asker == "print_specific":
            md_type = ask_utils.ask_specific_metadata()
            print()
            if md_type in exit_flags:
                return exit_flags[md_type]
            else:
                print_dir.print_specific_metadata_dir(dir_path, md_type)

        elif asker == "print_specific_recursive":
            md_type = ask_utils.ask_specific_metadata()
            print()
            if md_type in exit_flags:
                return exit_flags[md_type]
            else:
                temp = PrintDirRecursive()
                temp.print_specific_metadata_dir_recur(dir_path, md_type)
                print()

        elif asker in exit_flags:
            return exit_flags[asker]


def append_loop(dir_path: Path) -> bool:
    exit_flags = {
        "return": False,
        "exit": True}

    while True:
        asker = ask_append.ask_append_loop()
        print("\n")
        if asker == "append_metadata":
            md_type = ask_utils.ask_specific_metadata()
            print()
            if md_type in exit_flags:
                return exit_flags[md_type]
            else:
                md_text = ask_utils.ask_metadata_text()
                print("\n")
                append_dir.append_metadata_dir(dir_path, md_type, md_text)
                print("\n")

        elif asker == "append_metadata_recursive":
            md_type = ask_utils.ask_specific_metadata()
            print()
            if md_type in exit_flags:
                return exit_flags[md_type]
            else:
                md_text = ask_utils.ask_metadata_text()
                print("\n")
                temp = AppendingRecurrers()
                temp.append_metadata_dir_recur(dir_path, md_type, md_text)
                print("\n")

        elif asker == "append_tracknumber":
            append_dir.append_tracknum_dir(dir_path)

        elif asker == "append_tracknumber_recursive":
            temp = AppendingRecurrers()
            temp.append_tracknum_dir_recur(dir_path)

        elif asker == "append_date_recursive":
            temp = AppendingRecurrers()
            temp.append_date_dir_recur(dir_path)

        elif asker == "append_album_recursive":
            temp = AppendingRecurrers()
            temp.append_album_dir_recur(dir_path)

        elif asker == "append_title":
            del_until = ask_append.ask_del_until()
            print("\n")
            append_dir.append_title_dir(dir_path, del_until)

        elif asker == "append_title_recursive":
            temp = AppendingRecurrers()
            temp.append_title_dir_recur(dir_path)

        elif asker in exit_flags:
            return exit_flags[asker]


def removal_loop(dir_path: Path) -> bool:
    exit_flags = {
        "return": False,
        "exit": True}

    while True:
        removal_type = ask_removal.ask_removal_loop_dir()
        print("\n")

        exit_flags = {"return": False,
                      "exit": True}
        if removal_type in exit_flags:
            return exit_flags[removal_type]

        if removal_type == "all":
            remove_dir.remove_all_md_dir(dir_path)
            print("All existing audio metadata has been successfully removed\n\n")

        if removal_type == "all_recursive":
            temp = RemovalRecurrers()
            temp.remove_all_dir_recur(dir_path)

        elif removal_type == "appendable":
            remove_dir.remove_appendable_md_file(dir_path)
            print("All appendable audio metadata has been successfully removed\n\n")

        elif removal_type == "appendable_recursive":
            temp = RemovalRecurrers()
            temp.remove_appendable_dir_recur(dir_path)

        elif removal_type == "specific":
            all_keys = file_utils.get_audio_keys_dir(dir_path)
            print_dir.print_all_md_keys_dir(all_keys)
            print()

            md_to_del = ask_removal.ask_md_to_del(all_keys)
            if md_to_del == "return":
                print("\n")
                continue

            remove_dir.remove_specific_md_file(dir_path, md_to_del)
            print(f"\n{md_to_del} metadata has been successfully removed\n\n")

        elif removal_type == "specific_recursive":
            pass


def directory_loop(dir_path: Path) -> bool:
    while True:
        asker = ask_main.ask_main_dir_action(dir_path)
        print("\n")
        if asker == "print":
            exit_flag = print_loop(dir_path)
            if exit_flag:
                return True

        elif asker == "append":
            exit_flag = append_loop(dir_path)
            if exit_flag:
                return True

        elif asker == "remove":
            print("Work in progress")
            exit_flag = removal_loop(dir_path)
            if exit_flag == True:
                return True

        else:
            exit_flags = {
                "change_path": False,
                "exit": True}

            if asker in exit_flags:
                return exit_flags[asker]
