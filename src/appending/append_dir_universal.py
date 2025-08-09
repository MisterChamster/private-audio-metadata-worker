from src.file_ops.utils import (get_audios_from_dir,
                                print_audiofiles_in_dir)
from pathlib import Path
from src.appending.append_single_universal import append_metadata_file_universal
from src.utils import (get_tracknumber,
                       get_song_title)
from src.askers.utils_askers import ask_accept
from src.askers.appending_askers import (ask_new_title,
                                         ask_accept_or_change_name,
                                         ask_del_until,
                                         ask_decline_or_date,
                                         ask_date_action,
                                         ask_decline_or_album,
                                         ask_album_action)
from src.utils import get_album_date, get_album_name
import os



def append_metadata_dir(dir_path: str, md_type: str, md_text: str):
    files_list = get_audios_from_dir(dir_path)
    for filename in files_list:
        print(filename)
        file_path = str(Path(dir_path) / filename)
        append_metadata_file_universal(file_path, md_type, md_text)
    print()


def append_tracknum_dir(dir_path: str):
    files_list = get_audios_from_dir(dir_path)
    tracknums_list = []
    for filename in files_list:
        try:
            tracknums_list.append(get_tracknumber(filename))
        except Exception as e:
            print(f"Getting track number from {filename} caused an error: {e}")
            tracknums_list.append(None)

    for i in range(len(files_list)):
        print(f"Number: {tracknums_list[i]} for track: {files_list[i]}")
    print()

    user_accept = ask_accept()
    print()
    if not user_accept:
        return

    for i in range(len(files_list)):
        if tracknums_list[i] is not None:
            file_path = str(Path(dir_path) / files_list[i])
            append_metadata_file_universal(file_path, "tracknumber", tracknums_list[i])


def append_title_dir(dir_path: str):
    files_list = get_audios_from_dir(dir_path)
    titles_list = []

    print("Audio files in directory:")
    print_audiofiles_in_dir(dir_path)
    print()

    del_until = ask_del_until()
    print()

    for filename in files_list:
        try:
            titles_list.append(get_song_title(filename, del_until))
        except Exception as e:
            print(f"Getting title from {filename} caused an error: {e}")
            titles_list.append(None)

    while True:
        print("\n\n")
        for i in range(len(files_list)):
            print(f"Nr: {str(i+1):<2} Title: {titles_list[i]:<30} for track: {files_list[i]}")
        print()

        outer = ask_accept_or_change_name(len(files_list))
        print()
        if outer == "false":
            return
        elif outer == "true":
            break
        else:
            new_title_index = int(outer) - 1
            new_title = ask_new_title()
            print()
            titles_list[new_title_index] = new_title

    for i in range(len(files_list)):
        if titles_list[i] is not None:
            file_path = str(Path(dir_path) / files_list[i])
            append_metadata_file_universal(file_path, "title", titles_list[i])


def append_date_dir(dir_path: str):
    files_list = get_audios_from_dir(dir_path)
    date_text = ""
    confirm_block = False

    try:
        date_text = get_album_date(dir_path)
        confirm_block = True
    except Exception as e:
        print(f"Can't get date. Error: {e}")
        print()
        outer = ask_decline_or_date()
        if outer == "no_append":
            return
        else:
            date_text = outer

    if confirm_block == True:
        print(f"Append date '{date_text}' to audio files in folder {os.path.basename(dir_path)}?")
        outer = ask_date_action()
        if outer != "accept":
            date_text = outer

    for i in range(len(files_list)):
        file_path = str(Path(dir_path) / files_list[i])
        append_metadata_file_universal(file_path, "date", date_text)


def append_album_dir(dir_path: str, del_until: str):
    files_list = get_audios_from_dir(dir_path)
    album_text = ""
    confirm_block = False

    try:
        album_text = get_album_name(dir_path, del_until)
        confirm_block = True
    except Exception as e:
        print(f"Can't get album name. Error: {e}")
        print()
        outer = ask_decline_or_album()
        if outer == "no_append":
            return
        else:
            album_text = outer

    if confirm_block == True:
        print(f"Append album name '{album_text}' to audio files in folder {os.path.basename(dir_path)}?")
        outer = ask_album_action()
        if outer != "accept":
            album_text = outer

    for i in range(len(files_list)):
        file_path = str(Path(dir_path) / files_list[i])
        append_metadata_file_universal(file_path, "album", album_text)
