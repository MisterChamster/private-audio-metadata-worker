from pathlib import Path

import src.utils_file_ops as file_ops



def print_all_metadata_file(file_path: Path) -> None:
    audio = file_ops.get_audio(file_path)
    md_keys = audio.keys()

    appendable_md = ['album', 'title', 'artist', 'tracknumber', 'date']
    present_not_appentable = []
    present_appentable = []
    for md in md_keys:
        if md in appendable_md:
            present_appentable.append(md)
        else:
            present_not_appentable.append(md)

    if len(present_not_appentable) > 0:
        present_not_appentable.sort()
        max_len_no_app = 1 + max(
            len(string)
            for string
            in present_not_appentable)
        padded_keys_no_app = [
            (string + ":").ljust(max_len_no_app)
            for string
            in present_not_appentable]

        for i, key in enumerate(present_not_appentable):
            print(f"{padded_keys_no_app[i]} '{audio[key][0]}'")

    print()
    if len(present_appentable) > 0:
        present_appentable.sort()
        max_len_app = 1 + max(
            len(string)
            for string
            in present_appentable)
        padded_keys_app = [
            (string + ":").ljust(max_len_app)
            for string
            in present_appentable]

        for i, key in enumerate(present_appentable):
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
