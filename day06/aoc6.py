from copy import deepcopy

from tqdm import trange


def get_input(path):
    with open(path, "r") as file:
        grid = [list(line.strip()) for line in file.readlines()]
        return grid


class Guard:
    def __init__(self, map):
        self.grid = map
        self.trajectory = set()
        self.positions = set()
        self.dir = "N"
        self.mov = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}
        self.rotate = {"N": "E", "E": "S", "S": "W", "W": "N"}
        self.pos = self._get_pos()
        self.escaped = False

    def _get_pos(self):
        for row_id, row in enumerate(self.grid):
            for col_id, col in enumerate(row):
                if col == "^":
                    self.grid[row_id][col_id] = "."
                    # self.trajectory.add(((row_id, col_id), "N"))
                    # self.positions.add((row_id, col_id))
                    return row_id, col_id
        raise ValueError("Guard not found")

    def _update_pos(self, dir):
        new_pos = self.pos[0] + dir[0], self.pos[1] + dir[1]
        return new_pos

    def _in_bounds(self, pos):
        x, y = pos
        return 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0])

    def _look_ahead(self):
        x, y = self._update_pos(self.mov[self.dir])
        if self._in_bounds((x, y)):
            return self.grid[x][y]
        return None

    def _rotate(self):
        self.dir = self.rotate[self.dir]

    def _move(self):
        x, y = self.mov[self.dir]
        self.pos = self.pos[0] + x, self.pos[1] + y

    def _time_step(self):
        ahead = self._look_ahead()
        if not ahead:
            self.escaped = True
            return
        if ahead == "#":
            self._rotate()
            return
        self._move()

    def escapes(self):
        while not self.escaped:
            self.trajectory.add((self.pos, self.dir))
            self.positions.add(self.pos)
            self._time_step()
            if (self.pos, self.dir) in self.trajectory and not self.escaped:
                return False
        return True

    def num_visited_states(self):
        return len(self.positions)


def phase_2():
    obstructions = 0
    for x in trange(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == ".":
                new_grid = deepcopy(grid)
                new_grid[x][y] = "#"
                new_guard = Guard(new_grid)
                if not new_guard.escapes():
                    obstructions += 1

    return obstructions


if __name__ == "__main__":
    grid = get_input("input.txt")
    phase_1_grid = deepcopy(grid)
    guard = Guard(phase_1_grid)
    print(guard.escapes())
    print(guard.num_visited_states())
    print(phase_2())
