from copy import copy


def get_input(path):
    with open(path, "r") as file:
        digits = [ch for ch in file.readline()]
        return digits[:-1]


def convert_filesystem(filesys):
    new_sys = []
    for id, ch in enumerate(filesys):
        if id % 2 == 0:
            new_sys += [str(id // 2)] * int(ch)
        else:
            new_sys += ["."] * int(ch)
    return new_sys


def phase_1(filesys):
    compacted_filesys = compact_filesys(filesys)
    check = checksum(compacted_filesys)
    print(f"Phase 1: {check}")


def compact_filesys(filesystem):
    compact = copy(filesystem)
    left = -1
    right = len(filesystem)
    while left < right:
        left = get_next_dot(compact, left)
        right = get_next_num(compact, right)
        if left < right:
            compact[left], compact[right] = compact[right], compact[left]
    return compact


def get_next_dot(filesysem, index):
    return filesystem.index(".", index + 1)


def get_next_num(filesystem, index):
    for id in range(index - 1, -1, -1):
        if filesystem[id].isdigit():
            return id


def checksum(filesystem):
    return sum([id * int(val) for id, val in enumerate(filesystem) if val != "."])


def shuffle(filesys):
    shuffled = filesys[:]
    right = len(filesys)
    while right > 0:
        left = get_next_dots(shuffled, 0)
        right = get_next_num(shuffled, right)
        size = get_size(shuffled, right)
        right = right - size + 1
        while left < right:
            space = get_space(shuffled, left)
            if space >= size:
                swap(shuffled, left, right, size)
                break
            else:
                left += space
                left = get_next_dots(shuffled, left)

    return shuffled


def get_next_dots(shuffled, left):
    length = len(shuffled)
    while shuffled[left] != "." and left < length - 1:
        left += 1
    return left


def get_size(shuffled, right):
    size = 1
    while shuffled[right - 1] == shuffled[right]:
        right -= 1
        size += 1
    return size


def get_space(shuffled, left):
    space = 0
    while shuffled[left] == ".":
        space += 1
        left += 1
    return space


def swap(shuffled, left, right, size):
    for i in range(size):
        shuffled[left + i], shuffled[right + i] = (
            shuffled[right + i],
            shuffled[left + i],
        )


def phase_2(filesys):
    shuffled_filesys = shuffle(filesys)
    check = checksum(shuffled_filesys)
    print(f"Phase 2: {check}")


if __name__ == "__main__":
    filesystem = get_input("input.txt")
    filesystem = convert_filesystem(filesystem)
    phase_1(filesystem)
    # phase_2(filesystem)
