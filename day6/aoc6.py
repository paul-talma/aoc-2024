from copy import deepcopy


def get_input(path):
    with open(path, "r") as file:
        grid = [list(line) for line in file.readlines()]
        return grid


class Board:
    def __init__(self, grid):
        self.grid = grid
        self.next_dirs = {
            (0, -1): (-1, 0),
            (-1, 0): (0, 1),
            (0, 1): (1, 0),
            (1, 0): (0, -1),
        }
        self.guard_dir = (-1, 0)
        self.guard_pos = self.get_guard_pos()
        self.unique_visits = 1
        self.trajectory = set()

    def get_guard_direction(self):
        for dir in self.directions.keys():
            if dir in self.grid:
                return self.directions[dir]

    def get_guard_pos(self):
        for x, row in enumerate(self.grid):
            for y, elem in enumerate(row):
                if elem == "^":
                    return x, y
        raise ValueError("guard not found")

    def next_pos(self):
        return (
            self.guard_pos[0] + self.guard_dir[0],
            self.guard_pos[1] + self.guard_dir[1],
        )

    def in_bounds(self, x, y):
        return 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0])

    def check_guard_front(self):
        x, y = self.next_pos()
        if self.in_bounds(x, y):
            return self.grid[x][y]
        return None

    def rotate_guard(self):
        self.guard_dir = self.next_dirs[self.guard_dir]

    def mark_guard_pos(self):
        x, y = self.guard_pos
        self.grid[x][y] = "X"

    def move_guard(self):
        x = self.guard_pos[0] + self.guard_dir[0]
        y = self.guard_pos[1] + self.guard_dir[1]
        self.guard_pos = x, y

    def step_guard(self):
        next_item = self.check_guard_front()
        if not next_item:
            return False
        if next_item == "#":
            self.rotate_guard()
            return True
        if next_item == ".":
            self.unique_visits += 1
        self.mark_guard_pos()
        self.move_guard()
        return True

    def walk_guard(self):
        while self.step_guard():
            pass

    def get_grid(self):
        return self.grid

    def has_loop(self):
        while True:
            self.trajectory.add((self.guard_pos, self.guard_dir))
            end = not self.step_guard()
            if (self.guard_pos, self.guard_dir) in self.trajectory:
                return True
            if end:
                return False


def phase_2():
    traps = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == ".":
                new_grid = deepcopy(initial_grid)
                new_grid[x][y] = "#"
                new_board = Board(new_grid)
                if new_board.has_loop():
                    traps += 1
    return traps


if __name__ == "__main__":
    initial_grid = get_input("input.txt")
    grid = deepcopy(initial_grid)
    board = Board(grid)
    board.walk_guard()
    print(f"Phase 1: {board.unique_visits}")
    num_traps = phase_2()
    print(f"Phase 2: {num_traps}")
