def ask_specific_metadata() -> str:
    returns_dict = {"al": "album",
                    "ti": "title",
                    "ar": "artist",
                    "tr": "tracknumber",
                    "da": "date",
                    "rt": "return"}

    while True:
        print("Choose metadata type:\n" \
              "al   - album\n" \
              "ti   - title\n" \
              "ar   - artist\n" \
              "tr   - tracknumber\n" \
              "da   - date\n" \
              "rt   - Return\n" \
              "exit - Exit program\n\n>> ", end="")
        asker = input()

        if asker in returns_dict:
            return returns_dict[asker]
        if asker == "exit":
            return None


def ask_metadata_text():
    print("Input text to append as metadata\n\n>> ", end="")
    asker = input()
    return asker
