from tkinter import filedialog
import os



def ask_file_or_dir():
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


def ask_path_filedialog(type: str, message: str):
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
