from pathlib import Path

import src.utils_file_ops as file_ops



def print_all_metadata_file(file_path: Path) -> None:
    audio = file_ops.get_audio(file_path)
    md_keys = audio.keys()

    appendable_md = ['album', 'title', 'artist', 'tracknumber', 'date']
    present_not_appendable = []
    present_appendable = []
    for md in md_keys:
        if md in appendable_md:
            present_appendable.append(md)
        else:
            present_not_appendable.append(md)

    # Print non-appendable keys
    if len(present_not_appendable) > 0:
        present_not_appendable.sort()
        max_len_no_app = 1 + max(
            len(string)
            for string
            in present_not_appendable)
        padded_keys_no_app = [
            (string + ":").ljust(max_len_no_app)
            for string
            in present_not_appendable]

        for i, key in enumerate(present_not_appendable):
            print(f"{padded_keys_no_app[i]} '{audio[key][0]}'")

    # Print appendable keys
    print()
    if len(present_appendable) > 0:
        present_appendable.sort()
        max_len_app = 1 + max(
            len(string)
            for string
            in present_appendable)
        padded_keys_app = [
            (string + ":").ljust(max_len_app)
            for string
            in present_appendable]

        for i, key in enumerate(present_appendable):
            print(f"{padded_keys_app[i]} '{audio[key][0]}'")


def print_appendable_metadata_file(file_path: Path) -> None:
    audio = file_ops.get_audio(file_path)

    appendable_md = ['album', 'title', 'artist', 'tracknumber', 'date']
    max_len = len('tracknumber')
    for key in appendable_md:
        addstr = (max_len-len(key)) * " "
        if key in audio:
            print(f"{key}:{addstr} '{audio[key][0]}'")
        else:
            print(f"{key}:{addstr} Unavailable")


def print_specific_metadata_file(file_path: Path, md_name: str) -> None:
    audio = file_ops.get_audio(file_path)

    if md_name in audio:
        print(f"{md_name}: '{audio[md_name][0]}'")
    else:
        print(f"{md_name}: Unavailable")
