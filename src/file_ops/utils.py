import os



def get_audios_from_dir(dir_path: str, sort_it: bool = True) -> list:
    og_path = os.getcwd()
    os.chdir(dir_path)

    valid_exts = ["mp3", "flac"]
    audios_in_dir = []
    for node in os.listdir():
        if node.split(".")[-1] in valid_exts:
            audios_in_dir.append(node)
    if sort_it:
        audios_in_dir.sort()
    os.chdir(og_path)
    return audios_in_dir


def get_dirs_from_dir(dir_path: str, sort_it: bool = True) -> list:
    og_path = os.getcwd()
    os.chdir(dir_path)
    dirs_list = [node for node in os.listdir() if os.path.isdir(node)]
    if sort_it:
        dirs_list.sort()
    os.chdir(og_path)
    return dirs_list


def is_audio_in_dir(dir_path: str) -> bool:
    og_path = os.getcwd()
    os.chdir(dir_path)

    valid_exts = ["mp3", "flac"]
    for node in os.listdir():
        if node.split(".")[-1] in valid_exts:
            os.chdir(og_path)
            return True

    os.chdir(og_path)
    return False


def print_audiofiles_in_dir(dir_path: str):
    valid_extensions = ('mp3', 'heic')

    for filename in os.listdir(dir_path):
        if filename.lower().endswith(valid_extensions):
            print(filename)
