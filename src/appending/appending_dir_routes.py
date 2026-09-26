from pathlib import Path

import src.askers.askers_utils        as ask_utils
import src.appending.append_dir_tools as append_dir



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


def append_tracknumber_route(dir_path: Path) -> None:
    append_dir.append_tracknum_dir(dir_path)


def append_date_route(dir_path: Path) -> None:
    append_dir.append_date_dir(dir_path)

