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
