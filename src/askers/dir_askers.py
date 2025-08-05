def ask_main_dir_action(dir_path: str):
    returns_dict = {"pm": "print",
                    "am": "append",
                    "cd": "change_dir"}

    while True:
        print(f"Current directory path: {dir_path}\n" \
               "Choose action:\n"\
               "pm   - Print metadata...\n"\
               "am   - Append metadata...\n"\
               "cd   - Change path\n"\
               "exit - Exit program\n>> ", end="")
        asker = input()

        if asker == "exit":
            return None
        elif asker in returns_dict:
            return returns_dict[asker]
        else:
            print("Incorrect input.\n\n")
