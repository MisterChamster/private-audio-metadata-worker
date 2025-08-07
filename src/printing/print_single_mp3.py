from mutagen.easyid3 import EasyID3



def print_specific_metadata_mp3(file_path: str, md_name: str) -> None:
    try:
        audio = EasyID3(file_path)

    except Exception as e:
        print(f"Reading metadata caused an error: {e}")
        return

    if audio is None:
        print(f"Failed to load MP3 file: {file_path}")
        return

    if md_name in audio:
        print(f"{md_name}: {audio[md_name]}")
    else:
        print(f"{md_name}: Unavailable")
