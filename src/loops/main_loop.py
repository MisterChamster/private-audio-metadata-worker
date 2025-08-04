from os import chdir
from src.askers.main_askers import ask_file_or_dir, ask_path_filedialog, ask_main_action
from src.loops.file_loops import file_loop
from src.loops.directory_loops import directory_loop



def main_loop():
    while True:
        print()
        path_type = ask_file_or_dir()
        main_path = ""
        if path_type == None:
            return
        else:
            if path_type == "file":
                main_path = ask_path_filedialog("f", "Choose mp3 or flac audio file")
                if main_path == "":
                    return
            elif path_type == "directory":
                main_path = ask_path_filedialog("d", "Choose audio directory")
                if main_path == "":
                    return
                chdir(main_path)


        # print()
        # print(f"Current directory: {main_path}")
        # action = ask_main_action()
        # if action == None:
        #     return
        # elif action == "print":
        #     outer = print_loop()
        #     if outer == None:
        #         return
        # elif action == "append":
        #     outer = append_loop()
        #     if outer == None:
        #         return
        # elif action == "change":
        #     continue
            # main_path = ask_path_filedialog("d", "Choose audio directory")
            # if main_path == "":
            #     return
            # chdir(main_path)
