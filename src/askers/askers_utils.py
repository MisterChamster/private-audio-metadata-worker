def ask_specific_metadata() -> str | None:
    returns_dict = {
        "ab": "album",
        "ti": "title",
        "ar": "artist",
        "tr": "tracknumber",
        "dt": "date",
        "rt": "return"}

    while True:
        print("Choose metadata type:\n"
              "ab   - album\n"
              "ti   - title\n"
              "ar   - artist\n"
              "tr   - tracknumber\n"
              "dt   - date\n"
              "rt   - Return\n"
              "exit - Exit program\n\n>> ", end="")
        asker = input().strip().lower()

        if asker in returns_dict:
            return returns_dict[asker]
        if asker == "exit":
            return None


def ask_metadata_text() -> str:
    print("Input text to append as metadata\n>> ", end="")
    asker = input()
    return asker
