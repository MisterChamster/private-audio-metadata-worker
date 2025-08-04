from tkinter import filedialog
import os



def ask_path_filedialog(type: str, message: str):
    original_path = os.getcwd()
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    os.chdir(desktop_path)

    sel_path = ""
    if type == "f":
        sel_path = filedialog.askopenfilename(title=message)
    elif type == "d":
        sel_path = filedialog.askdirectory(title=message)

    os.chdir(original_path)
    return sel_path


def ask_main_action():
    returns_dict = {"prt": "print",
                    "amd": "append",
                    "cd": "changedir"}

    while True:
        print("Choose action:\n" \
              "prt  - Print metadata...\n" \
              "amd  - Append metadata...\n" \
              "cd   - Change directory...\n" \
              "exit - Exit program", end="")
        asker = input()

        if asker == "exit":
            return None
        elif asker not in ["prt", "amd", "cd"]:
            print("Incorrect input.\n")
        else:
            return returns_dict[asker]
