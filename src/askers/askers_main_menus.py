from tkinter import filedialog
from pathlib import Path
from typing  import Literal
from os import chdir, path



def ask_file_or_dir() -> Literal[
    "file",
    "directory",
    "exit"]:
    returns_dict = {
        "f": "file",
        "d": "directory",
        "e": "exit"}

    while True:
        print("Choose path type:\n"
              "f - File\n"
              "d - Directory\n"
              "e - Exit program\n>> ", end="")
        asker = input().strip().lower()

        if asker in returns_dict:
            return returns_dict[asker]
        else:
            print("Incorrect input.\n\n")


def ask_path_filedialog(
    node_type: Literal["file", "dir"]) -> Path | None:

    original_path = Path.cwd()
    search_begin_path = Path(path.expanduser("~")) / "Desktop"
    chdir(search_begin_path)

    selected_path = ""
    if node_type == "file":
        message = "Choose mp3 or flac audio file"
        selected_path = filedialog.askopenfilename(
            title=message,
            filetypes=[("Audio files",
                        "*.mp3 *.flac")])

        if selected_path == "":
            return
        selected_path = Path(selected_path)


    elif node_type == "dir":
        message = "Choose audio directory"
        selected_path = filedialog.askdirectory(title=message)

        if selected_path == "":
            chdir(original_path)
            return
        selected_path = Path(selected_path)

    chdir(original_path)
    return selected_path


def ask_main_file_action(file_path: Path) -> Literal[
    "print_all",
    "print_appendable",
    "append",
    "change_path",
    "exit"]:
    returns_dict = {
        "pm": "print_all",
        "pa": "print_appendable",
        "am": "append",
        "cd": "change_path",
        "e":  "exit"}

    msg_filename = file_path.name
    while True:
        print(f"File path: {file_path}\n"
              f"File name: {msg_filename}\n\n"
               "Choose action:\n"
               "pm - Print all metadata of the file\n"
               "pa - Print all appendable metadata of the file\n"
               "am - Append metadata...\n"
               "cd - Change path\n"
               "e  - Exit program\n>> ", end="")
        asker = input().strip().lower()

        if asker in returns_dict:
            return returns_dict[asker]
        else:
            print("Incorrect input.\n\n")


def ask_main_dir_action(dir_path: Path) -> Literal[
    "print",
    "append",
    "change_path",
    "exit"]:
    returns_dict = {
        "pm": "print",
        "am": "append",
        "cd": "change_path",
        "e":  "exit"}

    msg_filename = dir_path.name
    while True:
        print(f"Directory path: {dir_path}\n"
              f"Directory name: {msg_filename}\n\n"
               "Choose action:\n"
               "pm - Print metadata...\n"
               "am - Append metadata...\n"
               "cd - Change path\n"
               "e  - Exit program\n>> ", end="")
        asker = input().strip().lower()

        if asker in returns_dict:
            return returns_dict[asker]
        else:
            print("Incorrect input.\n\n")


def ask_print_loop() -> Literal[
    "print_all",
    "print_all_recursive",
    "print_appendable",
    "print_appendable_recursive",
    "print_specific",
    "print_specific_recursive",
    "return",
    "exit"]:
    returns_dict = {
        "m":  "print_all",
        "mr": "print_all_recursive",
        "a":  "print_appendable",
        "ar": "print_appendable_recursive",
        "s":  "print_specific",
        "sr": "print_specific_recursive",
        "r":  "return",
        "e":  "exit"}

    while True:
        print("Choose printing option:\n"
              "m  - Print metadata of all files\n"
              "mr - Print metadata of all files recursively\n"
              "a  - Print appendable metadata of all files\n"
              "ar - Print appendable metadata of all files recursively\n"
              "s  - Print specific metadata of all files\n"
              "sr - Print specific metadata of all files recursively\n"
              "r  - Return\n"
              "e  - Exit program\n>> ", end="")
        asker = input().strip().lower()

        if asker in returns_dict:
            return returns_dict[asker]
        else:
            print("Incorrect input\n\n")
