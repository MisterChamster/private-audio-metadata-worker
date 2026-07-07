from typing import Literal



def ask_removal_loop() -> Literal[
    "all",
    "appendable",
    "specific",
    "exit",
    "return"]:

    returns_dict = {
        "a": "all",
        "p": "appendable",
        "s": "specific",
        "r": "return",
        "x": "exit"}

    while True:
        print("Choose a removal option:\n"
              "a - All metadata\n"
              "p - Appendable metadata\n"
              "s - Specific metadata\n"
              "r - Return\n"
              "x - Exit program\n>> ", end="")
        asker = input().strip().lower()

        if asker in returns_dict:
            return returns_dict[asker]
        else:
            print("Incorrect input\n\n")


def ask_md_to_del(available_md: list[str]) -> str | Literal["return"]:
    returns_dict = {"r": "return"}

    while True:
        print("Choose a metadata to remove:\n"
              "(enter 'r' to return)\n>> ", end="")
        asker = input().strip().lower()

        if asker in returns_dict:
            return returns_dict[asker]
        elif asker in available_md:
            return asker
        else:
            print("Incorrect input\n\n")
