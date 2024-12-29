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


def safe_1(level):
    monotonic = all(increasing_at(level)) or all(decreasing_at(level))
    bounded = all(bounded_at(level))
    return monotonic and bounded


def part_1(levels):
    levels = [safe_1(level) for level in levels]
    print(sum(levels))


###################
#     part 2      #
###################


def safe_2(level):
    safe = False
    for idx in range(len(level)):
        small_level = remove(level, idx)
        safe = safe_1(small_level)
        if safe:
            return True
    return safe


def part_2(levels):
    levels = [safe_2(level) for level in levels]
    print(sum(levels))


if __name__ == "__main__":
    levels = get_levels("input_2.txt")
    part_1(levels)
    part_2(levels)
