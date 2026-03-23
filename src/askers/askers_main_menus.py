from tkinter import filedialog
from pathlib import Path
from typing  import Literal
import os



def ask_file_or_dir() -> str | None:
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
    search_begin_path = Path(os.path.expanduser("~")) / "Desktop"
    os.chdir(search_begin_path)

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
            return
        selected_path = Path(selected_path)

    os.chdir(original_path)
    return selected_path


def ask_main_file_action(file_path: Path) -> str:
    returns_dict = {
        "pm": "print_all",
        "pa": "print_appendable",
        "am": "append",
        "cd": "change_path",
        "e":  "exit"}

    msg_filename = file_path.name
    while True:
        print(f"File path: {file_path}\n"
              f"File name: {msg_filename}\n"
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


def ask_main_dir_action(dir_path: Path) -> str:
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


def ask_print_loop() -> str:
    returns_dict = {
        "pm":  "print_all",
        "pmr": "print_all_recursive",
        "pa":  "print_appendable",
        "par": "print_appendable_recursive",
        "ps":  "print_specific",
        "psr": "print_specific_recursive",
        "rt":  "return",
        "e":   "exit"}

    while True:
        print("Choose printing option:\n"
              "pm  - Print metadata of all files\n"
              "pmr - Print metadata of all files recursively\n"
              "pa  - Print appendable metadata of all files\n"
              "par - Print appendable metadata of all files recursively\n"
              "ps  - Print specific metadata of all files\n"
              "psr - Print specific metadata of all files recursively\n"
              "rt  - Return\n"
              "e   - Exit program\n>> ", end="")
        asker = input().strip().lower()

        if asker in returns_dict:
            return returns_dict[asker]
        else:
            print("Incorrect input\n\n")
