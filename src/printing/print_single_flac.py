from mutagen.flac import FLAC



def print_specific_metadata_flac(file_path: str, md_name: str) -> None:
    try:
        audio = FLAC(file_path)

    except Exception as e:
        print(f"Reading metadata caused an error: {e}")
        return

    if audio is None:
        print(f"Failed to load FLAC file: {file_path}")
        return

    if md_name in audio:
        print(f"{md_name}: {audio[md_name]}")
    else:
        print(f"{md_name}: Unavailable")
