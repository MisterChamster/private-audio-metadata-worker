def ask_main_dir_action(dir_path: str):
    returns_dict = {"pm": "print",
                    "am": "append",
                    "cd": "change_path"}

    while True:
        print(f"Current directory path: {dir_path}\n" \
               "Choose action:\n"\
               "pm   - Print metadata...\n"\
               "am   - Append metadata...\n"\
               "cd   - Change path\n"\
               "exit - Exit program\n\n>> ", end="")
        asker = input()

        if asker == "exit":
            return None
        elif asker in returns_dict:
            return returns_dict[asker]
        else:
            print("Incorrect input.\n\n")


def ask_print_loop():
    returns_dict = {"pm":  "print_all",
                    "pmr": "print_all_recursive",
                    "pa":  "print_appendable",
                    "par": "print_appendable_recursive",
                    "ps":  "print_specific",
                    "psr": "print_specific_recursive",
                    "rt":  "return"}

    while True:
        print("Choose printing option:\n"\
              "pm   - Print metadata of all files\n"\
              "pmr  - Print metadata of all files recursively\n"\
              "pa   - Print appendable metadata of all files\n"\
              "par  - Print appendable metadata of all files recursively\n"\
              "ps   - Print specific metadata of all files\n"\
              "psr  - Print specific metadata of all files recursively\n"\
              "rt   - Return\n"\
              "exit - Exit program\n\n>> ", end="")
        asker = input()

        if asker == "exit":
            return None
        elif asker in returns_dict:
            return returns_dict[asker]
        else:
            print("Incorrect input\n\n")


def ask_append_loop():
    return
