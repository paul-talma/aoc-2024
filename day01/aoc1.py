from collections import Counter


def get_lists(path):
    with open(path, "r") as file:
        left, right = [], []
        for line in file.readlines():
            words = line.split()
            left.append(int(words[0]))
            right.append(int(words[1]))
    return left, right


def part_1():
    left, right = get_lists("input.txt")
    left.sort()
    right.sort()
    diffs = []
    for l, r in zip(left, right):
        diff = abs(l - r)
        diffs.append(diff)

    return sum(diffs)


def part_2():
    left, right = get_lists("input.txt")
    left = Counter(left)
    right = Counter(right)
    sum = 0
    for val in left:
        if val in right:
            sum += val * right[val]

    return sum


print(part_1())
print(part_2())
