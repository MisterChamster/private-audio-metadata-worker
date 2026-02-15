from os import chdir

import src.askers.askers_main_menus as ask_main
import src.askers.askers_appending  as ask_append
import src.askers.askers_utils      as ask_utils
import src.md_printers.print_dir_tools as printdir
from src.md_printers.print_dir_recursive import PrintDirRecursive
import src.appending.append_dir_tools as append_dir
from src.appending.append_recur_dir      import AppendRecurDir
from src.appending.append_recur_tracknum import AppendRecurTracknum
from src.appending.append_recur_title    import AppendRecurTitle
from src.appending.append_recur_date     import AppendRecurDate
from src.appending.append_recur_album    import AppendRecurAlbum



def print_loop(dir_path: str) -> str | None:
    while True:
        asker = ask_main.ask_print_loop()
        print()
        if asker == "print_all":
            printdir.print_all_metadata_dir(dir_path)
            print()

        elif asker == "print_all_recursive":
            temp = PrintDirRecursive()
            temp.print_all_metadata_dir_recur(dir_path)
            print()

        elif asker == "print_appendable":
            printdir.print_appendable_metadata_dir(dir_path)
            print()

        elif asker == "print_appendable_recursive":
            temp = PrintDirRecursive()
            temp.print_appendable_metadata_dir_recur(dir_path)
            print()

        elif asker == "print_specific":
            md_type = ask_utils.ask_specific_metadata()
            print()
            if md_type == "return" or md_type == None:
                return md_type
            else:
                printdir.print_specific_metadata_dir(dir_path, md_type)

        elif asker == "print_specific_recursive":
            md_type = ask_utils.ask_specific_metadata()
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
            return


def append_loop(dir_path: str) -> str | None:
    while True:
        asker = ask_append.ask_append_loop()
        print("\n")
        if asker == "append_metadata":
            md_type = ask_utils.ask_specific_metadata()
            print()
            if md_type == "return" or md_type == None:
                return md_type
            else:
                md_text = ask_utils.ask_metadata_text()
                print()
                append_dir.append_metadata_dir(dir_path, md_type, md_text)

        elif asker == "append_metadata_recursive":
            md_type = ask_utils.ask_specific_metadata()
            print()
            if md_type == "return" or md_type == None:
                return md_type
            else:
                md_text = ask_utils.ask_metadata_text()
                print()
                temp = AppendRecurDir()
                temp.append_metadata_dir_recur(dir_path, md_type, md_text)

        elif asker == "append_tracknumber":
            append_dir.append_tracknum_dir(dir_path)

        elif asker == "append_tracknumber_recursive":
            temp = AppendRecurTracknum()
            temp.append_tracknum_dir_recur(dir_path)

        elif asker == "append_date_recursive":
            temp = AppendRecurDate()
            temp.append_date_dir_recur(dir_path)

        elif asker == "append_album_recursive":
            temp = AppendRecurAlbum()
            temp.append_album_dir_recur(dir_path)

        elif asker == "append_title":
            del_until = ask_append.ask_del_until()
            print("\n")
            append_dir.append_title_dir(dir_path, del_until)

        elif asker == "append_title_recursive":
            temp = AppendRecurTitle()
            temp.append_title_dir_recur(dir_path)

        elif asker == "return":
            return asker

        elif asker == None:
            return


def directory_loop(dir_path: str) -> str | None:
    chdir(dir_path)
    while True:
        asker = ask_main.ask_main_dir_action(dir_path)
        print("\n")
        if asker == "print":
            outer = print_loop(dir_path)
            if outer == None:
                return

        elif asker == "append":
            outer = append_loop(dir_path)
            if outer == None:
                return

        elif asker == "change_path":
            return asker

        elif asker == None:
            return
