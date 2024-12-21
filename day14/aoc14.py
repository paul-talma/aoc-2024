import re

HEIGHT = 103
WIDTH = 101


def get_input(path):
    with open(path, "r") as file:
        lines = file.readlines()
        lines = [line.split() for line in lines]
        lines = [tuple(parse_data(s) for s in line) for line in lines]
        return lines


def parse_data(string):
    return tuple(int(num) for num in re.findall(r"-?\d+", string))


def phase1():
    positions = []
    for pos, vel in input:
        final_col = (pos[0] + 100 * vel[0]) % WIDTH
        final_row = (pos[1] + 100 * vel[1]) % HEIGHT
        positions.append((final_col, final_row))
    return count_quadrants(positions)


def count_quadrants(robot_positions):
    q1 = q2 = q3 = q4 = 0
    middle_row = HEIGHT // 2
    middle_col = WIDTH // 2
    for x, y in robot_positions:
        if x < middle_col and y < middle_row:
            q1 += 1
        elif x < middle_col and y > middle_row:
            q2 += 1
        elif x > middle_col and y > middle_row:
            q3 += 1
        elif x > middle_col and y < middle_row:
            q4 += 1
    return q1 * q2 * q3 * q4


def phase2():
    start, finish = 8000, 8200
    for i in range(start, finish):
        positions = []
        for pos, vel in input:
            final_col = (pos[0] + i * vel[0]) % WIDTH
            final_row = (pos[1] + i * vel[1]) % HEIGHT
            positions.append((final_col, final_row))

        if contains_line(positions):
            print(i)


def contains_line(positions):
    grid = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for x, y in positions:
        grid[y][x] += 1

    contains = False
    for line in grid:
        if sum(x > 0 for x in line) == 33:
            contains = True
    return contains


if __name__ == "__main__":
    input = get_input("input.txt")
    print(phase1())
    phase2()
