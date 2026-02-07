import os



def ask_main_file_action(file_path: str):
    returns_dict = {
        "pm": "print_all",
        "pa": "print_appendable",
        "am": "append",
        "cd": "change_path"}

    while True:
        print(f"File path: {file_path}\n" 
              f"File name: {os.path.basename(file_path)}\n\n"
               "Choose action:\n"
               "pm   - Print all metadata of the file\n"
               "pa   - Print all appendable metadata of the file\n"
               "am   - Append metadata...\n"
               "cd   - Change path\n"
               "exit - Exit program\n\n>> ", end="")
        asker = input().strip().lower()

        if asker == "exit":
            return None
        elif asker in returns_dict:
            return returns_dict[asker]
        else:
            print("Incorrect input.\n\n")
