from pathlib import Path
import os

import src.utils_file_ops as utils_file
from src.appending.append_single_tools import append_metadata_file_universal
import src.utils_common as utils_common
import src.askers.askers_appending as ask_append



def append_metadata_dir(dir_path: str, md_type: str, md_text: str) -> None:
    files_list = utils_file.get_audios_from_dir(dir_path)
    for filename in files_list:
        print(filename)
        file_path = str(Path(dir_path) / filename)
        append_metadata_file_universal(file_path, md_type, md_text)
    print()


def append_tracknum_dir(dir_path: str) -> None:
    files_list = utils_file.get_audios_from_dir(dir_path)
    tracknums_list = []
    for filename in files_list:
        try:
            tracknums_list.append(utils_common.get_tracknumber(filename))
        except Exception as e:
            print(f"Getting track number from {filename} caused an error: {e}")
            tracknums_list.append(None)

    for i in range(len(files_list)):
        print_num = tracknums_list[i] if tracknums_list[i] is not None else "None"
        print(f"Number: {print_num:<2} for: {files_list[i]}")
    print()

    outer = ask_append.ask_accept_tracknum()
    print()
    if outer == "decline":
        return
    elif outer == "alphabetical":
        for i in range(len(files_list)):
            file_path = str(Path(dir_path) / files_list[i])
            append_metadata_file_universal(file_path, "tracknumber", str(i+1))
        return

    for i in range(len(files_list)):
        if tracknums_list[i] is not None:
            file_path = str(Path(dir_path) / files_list[i])
            append_metadata_file_universal(file_path, "tracknumber", tracknums_list[i])


def append_title_dir(dir_path: str, del_until: str) -> None:
    files_list = utils_file.get_audios_from_dir(dir_path)
    titles_list = []

    for filename in files_list:
        try:
            titles_list.append(utils_common.get_song_title(filename, del_until))
        except Exception as e:
            print(f"Getting title from {filename} caused an error: {e}")
            titles_list.append(None)

    while True:
        for i in range(len(files_list)):
            print_title = f"'{titles_list[i]}'" if titles_list[i] is not None else "None"
            title_with_quotation = print_title
            print(f"Nr: {str(i+1):<2} Title: {title_with_quotation:<30} for: {files_list[i]}")
        print()

        outer = ask_append.ask_accept_or_change_name(len(files_list))
        print()
        if outer == "false":
            print("\n")
            return
        elif outer == "true":
            print("\n")
            break
        else:
            new_title_index = int(outer) - 1
            new_title = ask_append.ask_new_title()
            titles_list[new_title_index] = new_title
            print("\n\n")

    for i in range(len(files_list)):
        if titles_list[i] is not None:
            file_path = str(Path(dir_path) / files_list[i])
            append_metadata_file_universal(file_path, "title", titles_list[i])


def append_date_dir(dir_path: str) -> None:
    files_list = utils_file.get_audios_from_dir(dir_path)
    date_text = ""
    confirm_block = False

    try:
        date_text = utils_common.get_album_date(dir_path)
        confirm_block = True
    except Exception as e:
        print(f"Can't get date. Error: {e}")
        print()
        outer = ask_append.ask_decline_or_date()
        if outer == "no_append":
            return
        else:
            date_text = outer

    if confirm_block == True:
        print(f"Date extracted: '{date_text}'\n" \
              f"Folder name:    {os.path.basename(dir_path)}\n")
        outer = ask_append.ask_date_action()
        print("\n\n")
        if outer != "accept":
            date_text = outer

    for i in range(len(files_list)):
        file_path = str(Path(dir_path) / files_list[i])
        append_metadata_file_universal(file_path, "date", date_text)


def append_album_dir(dir_path: str, del_until: str) -> None:
    files_list = utils_file.get_audios_from_dir(dir_path)
    album_text = ""
    confirm_block = False

    try:
        album_text = utils_common.get_album_name(dir_path, del_until)
        confirm_block = True
    except Exception as e:
        print(f"Can't get album name. Error: {e}")
        print()
        outer = ask_append.ask_decline_or_album()
        if outer == "no_append":
            return
        else:
            album_text = outer

    if confirm_block == True:
        print(f"Album extracted: '{album_text}'\n" \
              f"Folder name:     {os.path.basename(dir_path)}\n")
        outer = ask_append.ask_album_action()
        if outer == "decline":
            return
        elif outer != "accept":
            album_text = outer

    for i in range(len(files_list)):
        file_path = str(Path(dir_path) / files_list[i])
        append_metadata_file_universal(file_path, "album", album_text)
