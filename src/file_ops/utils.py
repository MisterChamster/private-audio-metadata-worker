import os



def get_audios_from_dir(dir_path: str, sort_it: bool = True) -> list:
    valid_exts = ("mp3", "flac")
    audios_in_dir = []
    for node in os.listdir(dir_path):
        if node.split(".")[-1] in valid_exts and node[0] != ".":
            audios_in_dir.append(node)
    if sort_it:
        audios_in_dir.sort()

    return audios_in_dir


def print_audiofiles_in_dir(dir_path: str, sort_it: bool = True):
    audios_list = get_audios_from_dir(dir_path, sort_it)

    for filename in audios_list:
        print(filename)


def get_dirs_from_dir(dir_path: str, sort_it: bool = True) -> list:
    og_path = os.getcwd()
    os.chdir(dir_path)
    dirs_list = [node for node in os.listdir() if os.path.isdir(node)]
    if sort_it:
        dirs_list.sort()
    os.chdir(og_path)
    return dirs_list


def is_audio_in_dir(dir_path: str) -> bool:
    valid_exts = ("mp3", "flac")
    for node in os.listdir(dir_path):
        if node.split(".")[-1] in valid_exts and node[0] != ".":
            return True
    return False
