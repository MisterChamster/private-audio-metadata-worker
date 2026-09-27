from pathlib import Path

import src.askers.askers_utils        as ask_utils
import src.askers.askers_appending    as ask_append
import src.appending.append_dir_tools as append_dir
from src.appending.appending_recurrers   import AppendingRecurrers



exit_flags = {
    "return": False,
    "exit":   True}

def append_md_route(dir_path: Path) -> bool:
    md_type = ask_utils.ask_metadata_type()
    print()

    if md_type in exit_flags:
        return exit_flags[md_type]
    else:
        md_text = ask_utils.ask_metadata_text()
        print()
        append_dir.append_metadata_dir(dir_path, md_type, md_text)
        print()


def append_md_recursive_route(dir_path: Path) -> bool:
    md_type = ask_utils.ask_metadata_type()
    print()
    if md_type in exit_flags:
        return exit_flags[md_type]
    else:
        md_text = ask_utils.ask_metadata_text()
        print("\n")
        temp = AppendingRecurrers()
        temp.append_metadata_dir_recur(dir_path, md_type, md_text)
        print("\n")


def append_tracknumber_route(dir_path: Path) -> None:
    append_dir.append_tracknum_dir(dir_path)


def append_tracknumber_recursive_route(dir_path: Path) -> None:
    temp = AppendingRecurrers()
    temp.append_tracknum_dir_recur(dir_path)


def append_date_route(dir_path: Path) -> None:
    append_dir.append_date_dir(dir_path)


def append_date_recursive_route(dir_path: Path) -> None:
    temp = AppendingRecurrers()
    temp.append_date_dir_recur(dir_path)


def append_album_route(dir_path: Path) -> None:
    del_until = ask_append.ask_del_until()
    print("\n")
    append_dir.append_album_dir(dir_path, del_until)


def append_album_recursive_route(dir_path: Path) -> None:
    temp = AppendingRecurrers()
    temp.append_album_dir_recur(dir_path)


def append_artist_route(dir_path: Path) -> None:
    append_dir.append_artist_dir(dir_path)


def append_artist_recursive_route(dir_path: Path) -> None:
    temp = AppendingRecurrers()
    temp.append_artist_dir_recur(dir_path)


def append_title_route(dir_path: Path) -> None:
    del_until = ask_append.ask_del_until()
    print("\n")
    append_dir.append_title_dir(dir_path, del_until)


def append_title_recursive_route(dir_path: Path) -> None:
    temp = AppendingRecurrers()
    temp.append_title_dir_recur(dir_path)
