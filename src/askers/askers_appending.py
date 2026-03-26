from typing import Literal



def ask_append_loop() -> Literal[
    "append_metadata",
    "append_metadata_recursive",
    "append_tracknumber",
    "append_tracknumber_recursive",
    "append_date_recursive",
    "append_album_recursive",
    "append_title",
    "append_title_recursive",
    "return",
    "exit"]:
    returns_dict = {
        "m":   "append_metadata",
        "mr":  "append_metadata_recursive",
        "t":   "append_tracknumber",
        "tr":  "append_tracknumber_recursive",
        "dr":  "append_date_recursive",
        "ar":  "append_album_recursive",
        "ti":  "append_title",
        "tir": "append_title_recursive",
        "r":   "return",
        "e":   "exit"}

    while True:
        print("Choose append option:\n"
              "m   - Append specific metadata to all files\n"
              "mr  - Append specific metadata to all files recursively\n"
              "t   - Append tracknumber based on filename\n"
              "tr  - Append tracknumber based on filename recursively\n"
              "dr  - Append date based on folder name recursively\n"
              "ar  - Append album based on folder name recursively\n"
              "ti  - Append title based on filename\n"
              "tir - Append title based on filename recursively\n"
              "r   - Return\n"
              "e   - Exit program\n>> ", end="")
        asker = input().strip().lower()

        if asker in returns_dict:
            return returns_dict[asker]
        else:
            print("Incorrect input\n\n")


def ask_new_title() -> str:
    print("Input new title\n>> ", end="")
    asker = input()
    return asker


def ask_accept_or_change_name(max_num: int) -> str:
    returns_dict = {
        "y": "true",
        "n": "false"}

    while True:
        print("Accept? (y/n)\n"
              "Input a file's number to manually change title\n>> ", end="")
        asker = input().strip()

        if asker in returns_dict:
            return returns_dict[asker]
        elif asker.isdigit():
            if asker[0] == "0":
                print("Incorrect input\n\n")
            elif int(asker) > max_num:
                print("Incorrect input\n\n")
            else:
                return asker
        else:
            print("Incorrect input\n\n")


def ask_del_until() -> Literal[" ", ".", "-", ""]:
    returns_dict = {
        "us":  " ",
        "udt": ".",
        "uda": "-",
        "dm":  ""}

    while True:
        print("Choose what to do with characters from the start:\n"
              "us  - Omit until first space\n"
              "udt - Omit until first '.'\n"
              "uda - Omit until first '-'\n"
              "dm  - Don't omit\n>> ", end="")
        asker = input().strip().lower()

        if asker in returns_dict:
            return returns_dict[asker]
        else:
            print("Incorrect input\n\n")


def ask_decline_or_date() -> str:
    while True:
        print("Leave empty to not append date or input your own date (year)\n>> ", end="")
        asker = input()

        if asker == "":
            return "no_append"
        elif (len(asker) == 4 and
              asker.isdigit() and
              asker[0] != "0"):
            return asker


def ask_date_action() -> str:
    while True:
        print("Leave empty to accept date or input your own date (year)\n>> ", end="")
        asker = input().strip()

        if asker == "":
            return "accept"
        elif (len(asker) == 4 and
              asker.isdigit() and
              asker[0] != "0"):
            return asker


def ask_decline_or_album() -> str:
    print("Leave empty to not append album name or input your own album name\n>> ", end="")
    asker = input()

    if asker == "":
        return "no_append"
    else:
        return asker


def ask_album_action() -> str:
    returns_dict = {
        "":  "accept",
        "d": "decline"}
    print("Leave empty to accept, input (d) to decline or input different name\n>> ", end="")
    asker = input().strip()

    if asker in returns_dict:
        return returns_dict[asker]
    else:
        return asker


def ask_accept_tracknum() -> Literal[
    "accept",
    "decline",
    "alphabetical"]:
    returns_dict = {
        "": "accept",
        "d": "decline",
        "a": "alphabetical"}

    while True:
        print("Leave empty to accept, input (d) to decline.\n"
              "Input (a) to use alphabetical order instead\n>> ", end="")
        asker = input().strip().lower()

        if asker in returns_dict:
            return returns_dict[asker]
        else:
            print("Incorrect input\n\n")
