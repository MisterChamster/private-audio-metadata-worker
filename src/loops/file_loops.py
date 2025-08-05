from src.askers.file_askers import ask_main_file_action



def append_loop():
    while True:
        return None


def file_loop(file_path: str):
    while True:
        asker = ask_main_file_action(file_path)
        if asker == "print":
            pass

        elif asker == "append":
            outer = append_loop()
            if outer == None:
                return None

        elif asker == "change_path":
            return asker

        elif asker == None:
            return None

        # For testing
        return None
