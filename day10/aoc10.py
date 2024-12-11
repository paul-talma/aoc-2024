def get_input(path):
    with open(path, "r") as file:
        return [[int(e) for e in line.strip()] for line in file.readlines()]


def phase_1():
    score = 0
    for x, row in enumerate(grid):
        for y, elem in enumerate(row):
            if elem == 0:
                score += get_score((x, y))
    print(f"Phase 1: {score}")


def get_score(pos):
    score = score_helper(pos, set())
    return score


def score_helper(pos, peaks):
    height = get_height(pos)
    if height == 9:
        peaks.add(pos)
    for next_pos in neighbors(pos, height):
        score_helper(next_pos, peaks)
    return len(peaks)


def get_height(pos):
    return grid[pos[0]][pos[1]]


def neighbors(pos, height):
    neighbors = []
    for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        x, y = pos[0] + i, pos[1] + j
        if in_bounds(x, y) and get_height((x, y)) == height + 1:
            neighbors.append((x, y))
    return neighbors


def in_bounds(x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


def phase_2():
    sum_ratings = 0
    for x, row in enumerate(grid):
        for y, elem in enumerate(row):
            if elem == 0:
                sum_ratings += get_rating((x, y))
    print(f"Phase 2: {sum_ratings}")


def get_rating(pos):
    current_path = [pos]
    rating = rating_helper(pos, [], current_path)
    return rating


def rating_helper(pos, paths, current_path):
    height = get_height(pos)
    current_path.append(pos)
    if height == 9:
        paths.append(current_path)
    for next_pos in neighbors(pos, height):
        rating_helper(next_pos, paths, current_path)
    return len(paths)


if __name__ == "__main__":
    grid = get_input("input.txt")
    phase_1()
    phase_2()
