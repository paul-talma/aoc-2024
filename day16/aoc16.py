from queue import PriorityQueue

L = ("L", 1000)
R = ("R", 1000)
F = ("F", 1)

actions = [L, R, F]

N = (-1, 0)
E = (0, 1)
S = (1, 0)
W = (0, -1)

turns = {
    (N, L): W,
    (N, R): E,
    (E, L): N,
    (E, R): S,
    (S, L): E,
    (S, R): W,
    (W, L): S,
    (W, R): N,
}


def get_map(path):
    with open(path, "r") as file:
        lines = file.readlines()
        return lines


def get_start_and_goal(grid):
    goal_found = False
    start_found = False
    goal_x = goal_y = start_x = start_y = 0
    for x, row in enumerate(grid):
        for y, elem in enumerate(row):
            if elem == "E":
                goal_x, goal_y = x, y
                goal_found = True
            if elem == "S":
                start_x, start_y = x, y
                start_found = True
            if goal_found and start_found:
                return (start_x, start_y), (goal_x, goal_y)


class State:
    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir

    def __str__(self):
        return f"Pos: ({self.x}, {self.y}), Dir: {self.dir}"

    def __repr__(self):
        return self.__str__()


def clear(state, dir):
    return grid[state.x + dir[0]][state.y + dir[1]] == "."


def valid(state, action):
    if action == F:
        return clear(state, state.dir)
    return clear(state, turns[(state.dir, action)])


def update_state(state, action):
    if action == F:
        state.x += state.dir[0]
        state.y += state.dir[1]
        return state
    state.dir = turns[(state.dir, action)]
    return state


def is_goal(state, goal):
    return state.x, state.y == goal[0], goal[1]


def UCS(start_state, goal_pos):
    pq = PriorityQueue((0, start_state))
    visited = set()
    while pq:
        curr_cost, curr_state = pq.get()
        visited.add((curr_state.x, curr_state.y))
        for action in actions:
            if valid(curr_state, action):
                next_state = update_state(curr_state, action)
                if is_goal(next_state, goal_pos):
                    return curr_cost + 1
                if (next_state.x, next_state.y) not in visited:
                    cost = curr_cost + action[1]
                    pq.put((cost, curr_state))


if __name__ == "__main__":
    grid = get_map("test.txt")
    start_pos, goal_pos = get_start_and_goal(grid)
    start_state = State(*start_pos, E)
    path_cost = UCS(start_state, goal_pos)
