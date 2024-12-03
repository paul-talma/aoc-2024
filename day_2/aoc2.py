import numpy as np

###################
# data processing #
###################


def get_levels(path):
    with open(path, "r") as file:
        levels = []
        for line in file.readlines():
            level = line.split()
            level = np.array(level, dtype=int)
            levels.append(level)
        return levels


#####################
# utility functions #
#####################


def remove(level, idx):
    return np.concat((level[:idx], level[idx + 1 :]))


def increasing_at(level):
    return level[:-1] < level[1:]


def decreasing_at(level):
    return level[:-1] > level[1:]


def bounded_at(level):
    return abs(level[:-1] - level[1:]) <= 3


###################
#     part 1      #
###################


def safe_level_1(level):
    monotonic = all(increasing_at(level)) or all(decreasing_at(level))
    bounded = all(bounded_at(level))
    return monotonic and bounded


def part_1(levels):
    levels = [safe_level_1(level) for level in levels]
    print(sum(levels))


###################
#     part 2      #
###################


def constant_at(level):
    return level[:-1] == level[1:]


def safe_level_2(level):
    # check for constant regions
    constant = np.argwhere(constant_at(level))  # indices x s.t. arr[x] == arr[x+1]
    if constant.size > 0:
        idx = constant[0, 0]
        level = remove(level, idx)
        return safe_level_1(level)

    # check for large jumps
    unbounded = np.argwhere(~bounded_at(level))  # indices x s.t. arr[x] << arr[x+1]
    if unbounded.size > 0:
        idx = unbounded[0, 0]
        if idx == 0:
            if abs(level[0] - level[1]) > abs(level[0] - level[2]):
                level = remove(level, 1)
                return safe_level_1(level)
            level = remove(level, idx)
            return safe_level_1(level)

        if abs(level[idx + 1] - level[idx - 1]) <= abs(level[idx + 1] - level[idx]):
            level = remove(level, idx)
            return safe_level_1(level)
        level = remove(level, idx + 1)
        return safe_level_1(level)

    # check for monotonicity
    increasing = np.argwhere(increasing_at(level))
    decreasing = np.argwhere(decreasing_at(level))
    if increasing.size > 1 and decreasing.size > 1:
        return False
    if increasing.size > 1:
        if decreasing.size == 0:
            return True
        idx = decreasing[0, 0]
        remove_left = remove(level, idx)
        remove_right = remove(level, idx + 1)
        return safe_level_1(remove_left) or safe_level_1(remove_right)
    if decreasing.size > 1:
        if increasing.size == 0:
            return True
        idx = increasing[0, 0]
        remove_left = remove(level, idx)
        remove_right = remove(level, idx + 1)
        return safe_level_1(remove_left) or safe_level_1(remove_right)
    return True


def part_2(levels):
    levels = [safe_level_2(level) for level in levels]
    print(sum(levels))


if __name__ == "__main__":
    levels = get_levels("input_2.txt")
    part_1(levels)
    part_2(levels)
