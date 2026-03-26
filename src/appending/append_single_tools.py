from pathlib import Path

import src.utils_file_ops as file_ops



def append_metadata_file_universal(
    file_path: Path,
    md_type: str,
    md_text: str
) -> None:
    # Safe against mac files ugh
    filename = file_path.name
    if filename.startswith("."):
        return

    audio = file_ops(file_path)

    audio[md_type] = md_text
    audio.save()
