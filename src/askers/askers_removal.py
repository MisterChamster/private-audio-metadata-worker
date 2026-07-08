from typing import Literal



def ask_removal_loop_file() -> Literal[
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


def ask_removal_loop_dir() -> Literal[
    "all",
    "all_recursive",
    "appendable",
    "appendable_recursive",
    "specific",
    "specific_recursive",
    "exit",
    "return"]:

    returns_dict = {
        "a":  "all",
        "ar": "all_recursive",
        "p":  "appendable",
        "pr": "appendable_recursive",
        "s":  "specific",
        "sr": "specific_recursive",
        "r":  "return",
        "x":  "exit"}

    while True:
        print("Choose a removal option:\n"
              "a  - All metadata\n"
              "ar - All metadata (recursive)\n"
              "p  - Appendable metadata\n"
              "pr - Appendable metadata (recursive)\n"
              "s  - Specific metadata\n"
              "sr - Specific metadata (recursive)\n"
              "r  - Return\n"
              "x  - Exit program\n>> ", end="")
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
