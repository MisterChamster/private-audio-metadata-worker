import os



# Put that one in a try block
def get_tracknumber(filename: str) -> str:
    """
    Gets track number from first digits of filename.

    Gets digits until a non digit, deletes 0s from beginning, returns rest.
    If every character is 0, returns 0
    """
    begin_nums = ""
    # Get digits from beginning of the file name
    for i in range(len(filename)):
        if filename[i].isdigit():
            begin_nums += filename[i]
        else:
            break

    if begin_nums == "":
        raise Exception("No numbers to extract tracknumber from")

    while begin_nums[0] == "0":
        # Delete zero from beginning
        begin_nums = begin_nums[1:]
        # If it was all zeros
        if begin_nums == "":
            return "0"

    return begin_nums


def get_song_title(filename: str, del_until: str) -> str:
    filename_no_ext = ".".join(filename.split(".")[:-1])

    # Nothing to delete
    if del_until == "":
        return filename_no_ext

    # Sign to del is in filename
    elif del_until in filename_no_ext:
        filename_split = filename_no_ext.split(del_until)
        # If del sign is the last character before extension
        if len(filename_split) <= 1:
            raise Exception(f"Deleting everything before '{del_until}' returns empty string")
        else:
            return del_until.join(filename_split[1:])

    # Sign to del is not in filename
    else:
        raise Exception(f"File name has no '{del_until}' signs")


def get_album_date(dir_path: str):
    dir_name = os.path.basename(dir_path)
    if ")" not in dir_name:
        raise Exception("Wrong folder name: no ')' sign.")

    end_col_list = [i for i, c in enumerate(dir_name) if c == ")"]
    if end_col_list[-1] <= 4:
        raise Exception("Wrong folder name, can't read date.")

    # Read 4 chars before ")"
    read_before = end_col_list[-1]
    date = dir_name[read_before-4: read_before]
    if not date.isdigit():
        raise Exception(f"Not all characters in {date} are digits")

    return date


def get_album_name(dir_path: str):
    dir_name = os.path.basename(dir_path)

    # Delete year
    if " (" in dir_name:
        last_startcolon_index = [i for i, c in dir_name if c == "("][-1]
        if last_startcolon_index <= 1:
            raise Exception("Wrong folder name, can't read album.")
        elif dir_name[last_startcolon_index-1] == " ":
            dir_name = dir_name[:last_startcolon_index-1]
