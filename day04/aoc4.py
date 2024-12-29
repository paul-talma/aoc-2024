def get_input(path):
    with open(path, "r") as file:
        return file.readlines()


# letter defs
X = "X"
M = "M"
A = "A"
S = "S"

# next letters
next_letters = {X: M, M: A, A: S}

# directions
directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1),
]


###############
#   Phase 1   #
###############


def search_word(position):
    """
    search for XMAS in every direction, sum results
    """
    return sum(map(lambda dir: search_next_letter(X, position, dir), directions))


def search_next_letter(current_letter, position, direction):
    """
    recursively check if next letter along direction is expected letter
    """
    if current_letter == S:
        return True

    x, y = next_pos(position, direction)
    if not in_bounds((x, y)):
        return False

    expected_letter = next_letters[current_letter]
    next_letter = grid[x][y]
    if next_letter != expected_letter:
        return False
    return search_next_letter(expected_letter, (x, y), direction)


def next_pos(curr_pos, direction):
    """
    increment current position by direction
    """
    return tuple(sum(x) for x in zip(curr_pos, direction))


def in_bounds(pos):
    """
    check if position is out of bounds
    """
    return -1 < pos[0] < n_rows and -1 < pos[1] < n_cols


def phase_1():
    total = 0
    for x in range(n_rows):
        for y in range(n_cols):
            if grid[x][y] == X:
                total += search_word((x, y))

    print(f"Phase 1: {total}")


###############
#   Phase 2   #
###############


def x_mas_check(pos):
    return diag1(pos) and diag2(pos)


def diag1(pos):
    """
    check top left to bottom right diagonal
    """
    x, y = pos
    MS = grid[x - 1][y - 1] == M and grid[x + 1][y + 1] == S
    SM = grid[x - 1][y - 1] == S and grid[x + 1][y + 1] == M
    return MS or SM


def diag2(pos):
    """
    check top right to bottom left diagonal
    """
    x, y = pos
    MS = grid[x - 1][y + 1] == M and grid[x + 1][y - 1] == S
    SM = grid[x - 1][y + 1] == S and grid[x + 1][y - 1] == M
    return MS or SM


def phase_2():
    total = 0
    for x in range(1, n_rows - 1):
        for y in range(1, n_cols - 1):
            if grid[x][y] == A:
                total += x_mas_check((x, y))

    print(f"Phase 2: {total}")


if __name__ == "__main__":
    grid = get_input("input.txt")
    n_rows, n_cols = len(grid), len(grid[0])
    phase_1()
    phase_2()
