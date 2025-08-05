from src.askers.main_askers import ask_file_or_dir, ask_path_filedialog
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
                outer = file_loop(main_path)

            elif path_type == "directory":
                main_path = ask_path_filedialog("d", "Choose audio directory")
                if main_path == "":
                    return
                outer = directory_loop(main_path)
