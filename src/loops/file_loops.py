from src.askers.file_askers import ask_main_file_action



def file_loop(file_path: str):
    while True:
        print(f"File path: {file_path}")
        outer = ask_main_file_action(file_path)
        if outer == None:
            return None
        return None
