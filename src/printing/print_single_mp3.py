from mutagen.easyid3 import EasyID3



def print_all_mp3(file_path: str) -> None:
    try:
        audio = EasyID3(file_path)

    except Exception as e:
        print(f"Reading metadata caused an error: {e}")
        return

    if audio is None:
        print(f"Failed to load MP3 file: {file_path}")
        return

    print()
    for key in audio:
        print(f"{key}: {audio[key]}")


def print_appendable_mp3(file_path: str) -> None:
    try:
        audio = EasyID3(file_path)

    except Exception as e:
        print(f"Reading metadata caused an error: {e}")
        return

    if audio is None:
        print(f"Failed to load MP3 file: {file_path}")
        return

    print()
    specific_md = ['album', 'tracknumber', 'title', 'artist', 'date']
    for key in specific_md:
        if key in audio:
            print(f"{key}: {audio[key]}")
        else:
            print(f"{key}: Unavailable")


def print_specific_mp3(file_path: str, md_name: str) -> None:
    try:
        audio = EasyID3(file_path)

    except Exception as e:
        print(f"Reading metadata caused an error: {e}")
        return

    if audio is None:
        print(f"Failed to load MP3 file: {file_path}")
        return

    print()
