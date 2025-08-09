def ask_append_loop():
    returns_dict = {"am":   "append_metadata",
                    "amr":  "append_metadata_recursive",
                    "at":   "append_tracknumber",
                    "atr":  "append_tracknumber_recursive",
                    "ati":  "append_title",
                    "atir": "append_title_recursive",
                    "adr":  "append_date_recursive",
                    "aar":  "append_album_recursive",
                    "rt":   "return"}

    while True:
        print("Choose append option:\n" \
            "am   - Append specific metadata to all files\n" \
            "amr  - Append specific metadata to all files recursively\n" \
            "at   - Append tracknumber based on filename\n" \
            "atr  - Append tracknumber based on filename recursively\n" \
            "ati  - Append title based on filename\n" \
            "atir - Append title based on filename recursively\n" \
            "adr  - Append date based on filename recursively\n" \
            "aar  - Append album based on filename recursively\n" \
            "rt   - Return\n" \
            "exit - Exit program\n\n>> ", end="")
        asker = input()

        if asker in returns_dict:
            return returns_dict[asker]
        elif asker == "exit":
            return None
        else:
            print("Incorrect input\n\n")


def ask_new_title():
    print("Input new title\n>> ", end="")
    asker = input()
    return asker


def ask_accept_or_change_name(max_num: int) -> str:
    while True:
        print("Accept? (y/n)\n" \
              "Input a file's number to manually change title\n>> ", end="")
        asker = input()

        if asker == "y":
            return "true"
        elif asker == "n":
            return "false"
        elif asker.isdigit():
            if asker[0] == "0":
                print("Incorrect input\n\n")
            elif int(asker) >= max_num:
                print("Incorrect input\n\n")
            else:
                return asker
        else:
            print("Incorrect input\n\n")


def ask_del_until() -> str:
    returns_dict = {"us":  " ",
                    "udt": ".",
                    "uda": "-",
                    "dm":  ""}

    while True:
        print("Choose what to do with characters from the start:\n" \
              "us  - Omit until first space\n" \
              "udt - Omit until first '.'\n" \
              "uda - Omit until first '-'\n" \
              "dm  - Don't omit\n\n>> ", end="")
        asker = input()

        if asker in returns_dict:
            return returns_dict[asker]
        else:
            print("Incorrect input\n\n")


def ask_decline_or_date():
    while True:
        print("Press enter to not append date or input your own date (year)\n>> ", end="")
        asker = input()

        if asker == "":
            return "no_append"
        elif len(asker) == 4 and asker.isdigit() and asker[0] != "0":
            return asker


def ask_date_action():
    while True:
        print("Press enter to accept date or input your own date (year)\n>> ", end="")
        asker = input()

        if asker == "":
            return "accept"
        elif len(asker) == 4 and asker.isdigit() and asker[0] != "0":
            return asker


def ask_decline_or_album():
    while True:
        print("Press enter to not append album name or input your own album name\n>> ", end="")
        asker = input()

        if asker == "":
            return "no_append"
        else:
            return asker


def ask_album_action():
    while True:
        print("Press enter to accept album name or input your own name\n>> ", end="")
        asker = input()

        if asker == "":
            return "accept"
        elif len(asker) == 4 and asker.isdigit() and asker[0] != "0":
            return asker
