def get_input(path):
    with open(path, "r") as file:
        stones = file.readline().strip().split()
        return [int(s) for s in stones]


def memoize(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


def solve(array, max_depth):
    return sum(map(lambda x: rec(x, max_depth), array))


@memoize
def rec(val, depth):
    if depth == 0:
        return 1
    if val == 0:
        return rec(1, depth - 1)
    length = len(str(val))
    if length % 2 == 0:
        left, right = int(str(val)[: length // 2]), int(str(val)[length // 2 :])
        return rec(left, depth - 1) + rec(right, depth - 1)
    return rec(val * 2024, depth - 1)


if __name__ == "__main__":
    stones = get_input("input.txt")
    print(f"Phase 1, recursive: {solve(stones, 25)}")
    print(f"Phase 2, recursive: {solve(stones, 75)}")
