def ask_specific_metadata() -> str:
    returns_dict = {"ab": "album",
                    "ti": "title",
                    "ar": "artist",
                    "tr": "tracknumber",
                    "dt": "date",
                    "rt": "return"}

    while True:
        print("Choose metadata type:\n" \
              "ab   - album\n" \
              "ti   - title\n" \
              "ar   - artist\n" \
              "tr   - tracknumber\n" \
              "dt   - date\n" \
              "rt   - Return\n" \
              "exit - Exit program\n\n>> ", end="")
        asker = input()

        if asker in returns_dict:
            return returns_dict[asker]
        if asker == "exit":
            return None


def ask_metadata_text() -> str:
    print("Input text to append as metadata\n>> ", end="")
    asker = input()
    return asker


def ask_accept() -> bool:
    while True:
        print("Accept? (y/n)\n>> ", end="")
        asker = input()

        if asker == "y":
            return True
        elif asker == "n":
            return False
        else:
            print("Incorrect input\n\n")


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
