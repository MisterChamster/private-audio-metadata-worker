from tkinter import filedialog
import os



def ask_file_or_dir() -> str | None:
    returns_dict = {
        "f": "file",
        "d": "directory"}

    while True:
        print("Choose path type:\n"
              "f    - File\n"
              "d    - Directory\n"
              "exit - Exit program\n\n>> ", end="")
        asker = input().strip().lower()

        if asker == "exit":
            return None
        elif asker in returns_dict:
            return returns_dict[asker]
        else:
            print("Incorrect input.\n\n")


def ask_path_filedialog(type: str, message: str) -> str:
    original_path = os.getcwd()
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    os.chdir(desktop_path)

    selected_path = ""
    if type == "f":
        while True:
            selected_path = filedialog.askopenfilename(title=message)
            filename = os.path.basename(selected_path)

            if ((selected_path.endswith("mp3")) or
                (selected_path.endswith("flac")) or
                (selected_path == "")) and \
                (not filename.startswith(".")):
                break
            else:
                print("Incorrect file extension.")
    elif type == "d":
        selected_path = filedialog.askdirectory(title=message)

    os.chdir(original_path)
    return selected_path


def ask_main_file_action(file_path: str) -> str | None:
    returns_dict = {
        "pm": "print_all",
        "pa": "print_appendable",
        "am": "append",
        "cd": "change_path"}

    while True:
        print(f"File path: {file_path}\n" 
              f"File name: {os.path.basename(file_path)}\n\n"
               "Choose action:\n"
               "pm   - Print all metadata of the file\n"
               "pa   - Print all appendable metadata of the file\n"
               "am   - Append metadata...\n"
               "cd   - Change path\n"
               "exit - Exit program\n\n>> ", end="")
        asker = input().strip().lower()

        if asker == "exit":
            return None
        elif asker in returns_dict:
            return returns_dict[asker]
        else:
            print("Incorrect input.\n\n")


def ask_main_dir_action(dir_path: str) -> str | None:
    returns_dict = {
        "pm": "print",
        "am": "append",
        "cd": "change_path"}

    while True:
        print(f"Directory path: {dir_path}\n"
              f"Directory name: {os.path.basename(dir_path)}\n\n"
               "Choose action:\n"
               "pm   - Print metadata...\n"
               "am   - Append metadata...\n"
               "cd   - Change path\n"
               "exit - Exit program\n\n>> ", end="")
        asker = input().strip().lower()

        if asker == "exit":
            return None
        elif asker in returns_dict:
            return returns_dict[asker]
        else:
            print("Incorrect input.\n\n")


def ask_print_loop() -> str | None:
    returns_dict = {
        "pm":  "print_all",
        "pmr": "print_all_recursive",
        "pa":  "print_appendable",
        "par": "print_appendable_recursive",
        "ps":  "print_specific",
        "psr": "print_specific_recursive",
        "rt":  "return"}

    while True:
        print("Choose printing option:\n"
              "pm   - Print metadata of all files\n"
              "pmr  - Print metadata of all files recursively\n"
              "pa   - Print appendable metadata of all files\n"
              "par  - Print appendable metadata of all files recursively\n"
              "ps   - Print specific metadata of all files\n"
              "psr  - Print specific metadata of all files recursively\n"
              "rt   - Return\n"
              "exit - Exit program\n\n>> ", end="")
        asker = input().strip().lower()

        if asker == "exit":
            return None
        elif asker in returns_dict:
            return returns_dict[asker]
        else:
            print("Incorrect input\n\n")
