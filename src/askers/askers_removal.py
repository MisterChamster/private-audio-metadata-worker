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
