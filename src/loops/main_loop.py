import src.askers.askers_main_menus as askers
from src.loops.file_loops import file_loop
from src.loops.directory_loops import directory_loop



def main_loop() -> None:
    while True:
        print()
        path_type = askers.ask_file_or_dir()
        print("\n")
        if path_type == "exit":
            return

        if path_type == "file":
            file_path = askers.ask_path_filedialog("file")
            if not file_path:
                return
            outer = file_loop(file_path)
            if outer == "exit":
                return

        elif path_type == "directory":
            dir_path = askers.ask_path_filedialog("dir")
            if not dir_path:
                return
            outer = directory_loop(dir_path)
            if outer == "exit":
                return
