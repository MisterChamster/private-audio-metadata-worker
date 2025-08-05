from src.askers.file_askers import ask_main_file_action



def file_loop(file_path: str):
    while True:
        print(f"File path: {file_path}")
        asker = ask_main_file_action(file_path)
        if asker == "print":
            pass
        elif asker == "append":
            pass
        elif asker == "change_path":
            pass
        elif asker == None:
            return None

        # For testing
        return None
