def get_input(path):
    with open(path, "r") as file:
        stones = file.readline().strip().split()
        return [int(s) for s in stones]


def update(stones):
    new_stones = []
    for s in stones:
        if s == 0:
            new_stones.append(1)
        elif len(str(s)) % 2 == 0:
            new_stones.extend(rule2(s))
        else:
            new_stones.append(s * 2024)
    return new_stones


def rule2(stone):
    string_stone = str(stone)
    length = len(string_stone) // 2
    left, right = int(string_stone[:length]), int(string_stone[length:])
    return left, right


if __name__ == "__main__":
    stones = get_input("test.txt")
    stones1 = stones[:]
    for _ in range(25):
        stones1 = update(stones1)
    print(f"Phase 1: {len(stones1)}")
    for _ in range(75):
        stones = update(stones)
    print(f"Phase 2: {len(stones)}")
