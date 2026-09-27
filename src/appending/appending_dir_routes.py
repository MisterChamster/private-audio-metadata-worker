from pathlib import Path

import src.utils_common               as utils_common
import src.askers.askers_utils        as ask_utils
import src.askers.askers_appending    as ask_append
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


def append_album_route(dir_path: Path) -> None:
    del_until = ask_append.ask_del_until()
    print("\n")
    append_dir.append_album_dir(dir_path, del_until)


def append_artist_route(dir_path: Path) -> None:
    artist_names = utils_common.get_possible_artist_names(dir_path)
    range_size = len(artist_names) if len(artist_names) <= 3 else 3

    print("Choose artist name to append:")
    for i in range(range_size):
        print(f"{i+1} - {artist_names[i]}")
    print("r - Return\n>> ", end='')
    response = input().strip().lower()
    print()

    if response == "r":
        print("\n")
        return
    elif response.isdigit():
        response = int(response)
        if response == 0 or response > range_size:
            print("Incorrect input\n\n")
            return
        else:
            artist_name = artist_names[response-1]
            append_dir.append_metadata_dir(dir_path, "artist", artist_name)
            print("\n")
