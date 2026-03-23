def ask_specific_metadata() -> str:
    returns_dict = {
        "ab": "album",
        "ti": "title",
        "ar": "artist",
        "tr": "tracknumber",
        "dt": "date",
        "r":  "return",
        "e":  "exit"}

    while True:
        print("Choose metadata type:\n"
              "ab - album\n"
              "ti - title\n"
              "ar - artist\n"
              "tr - tracknumber\n"
              "dt - date\n"
              "r  - Return\n"
              "e  - Exit program\n>> ", end="")
        asker = input().strip().lower()

        if asker in returns_dict:
            return returns_dict[asker]
        else:
            print("Invalid input\n\n")


def ask_metadata_text() -> str:
    print("Input text to append as metadata\n>> ", end="")
    asker = input()
    return asker
