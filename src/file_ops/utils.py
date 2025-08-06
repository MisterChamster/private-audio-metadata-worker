import os



def get_audios_from_cwd(dir_path: str) -> list:
    og_path = os.getcwd()
    os.chdir(dir_path)

    valid_exts = ["mp3", "flac"]
    audios_in_cwd = []
    for node in os.listdir():
        if node.split(".")[-1] in valid_exts:
            audios_in_cwd.append(node)
    os.chdir(og_path)
    return audios_in_cwd
