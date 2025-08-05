from tkinter import filedialog
import os



def ask_file_or_dir():
    returns_dict = {"f": "file",
                    "d": "directory"}

    while True:
        print("Choose path type:\n" \
              "f    - File\n"       \
              "d    - Directory\n"  \
              "exit - Exit program\n>> ", end="")
        asker = input()

        if asker == "exit":
            return None
        elif asker not in ["f", "d"]:
            print("Incorrect input.\n")
        else:
            return returns_dict[asker]


def ask_path_filedialog(type: str, message: str):
    original_path = os.getcwd()
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    os.chdir(desktop_path)

    sel_path = ""
    if type == "f":
        while True:
            sel_path = filedialog.askopenfilename(title=message)
            if (sel_path.endswith("mp3")) or \
               (sel_path.endswith("flac")) or \
               (sel_path == ""):
                break
            else:
                print("Incorrect file extension.")
    elif type == "d":
        sel_path = filedialog.askdirectory(title=message)

    os.chdir(original_path)
    return sel_path
