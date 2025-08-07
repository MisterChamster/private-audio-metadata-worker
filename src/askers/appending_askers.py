def ask_append_loop():
    returns_dict = {"am":   "append_metadata",
                    "amr":  "append_metadata_recursive",
                    "at":   "append_tracknumber",
                    "atr":  "append_tracknumber_recursive",
                    "ati":  "append_title",
                    "atir": "append_title_recursive",
                    "rt":   "return"}

    print("Choose append option:\n" \
          "am   - Append specific metadata to all files\n" \
          "amr  - Append specific metadata to all files recursively\n" \
          "at   - Append tracknumber based on filename\n" \
          "atr  - Append tracknumber based on filename recursively\n" \
          "ati  - Append title based on filename\n" \
          "atir - Append title based on filename recursively\n" \
          "rt   - Return\n" \
          "exit - Exit program\n\n>> ", end="")
    asker = input()

    if asker in returns_dict:
        return returns_dict[asker]
    elif asker == "exit":
        return None
