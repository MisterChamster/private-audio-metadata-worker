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


def get_title(filename: str, del_until: str) -> str:
    filename_no_ext = "".join(filename.split(".")[:-1])

    if del_until == "":
        return filename_no_ext

    elif del_until in filename_no_ext:
        filename_split = filename_no_ext.split(del_until)
        if len(filename_split) <= 1:
            raise Exception(f"Deleting everything before '{del_until}' returns empty string")
        else:
            filename_split = filename_split[1:]
            return "".join(filename_split)

    else:
        raise Exception(f"File name has no '{del_until}' signs")
