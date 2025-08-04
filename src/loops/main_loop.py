from os import chdir
from src.askers.main_askers import ask_file_or_dir, ask_path_filedialog, ask_main_action
from src.loops.print_loops import print_loop
from src.loops.append_loops import append_loop



def main_loop():
    # print()
    while True:
        path_type = ask_file_or_dir()
        dir_main = ""
        if path_type == None:
            return
        else:
            if path_type == "file":
                dir_main = ask_path_filedialog("f", "Choose audio file")
            elif path_type == "directory":
                dir_main = ask_path_filedialog("d", "Choose audio directory")

            if dir_main == "":
                return
            chdir(dir_main)



        print()
        print(f"Current directory: {dir_main}")
        action = ask_main_action()
        if action == None:
            return
        elif action == "print":
            outer = print_loop()
            if outer == None:
                return
        elif action == "append":
            outer = append_loop()
            if outer == None:
                return
        elif action == "change":
            dir_main = ask_path_filedialog("d", "Choose audio directory")
            if dir_main == "":
                return
            chdir(dir_main)
