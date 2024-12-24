import re

MAX = 100_000_000_000_000


class Button:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def get_input(path):
    with open(path, "r") as file:
        lines = file.readlines()
        data = []
        for i in range(0, len(lines), 4):
            x, y = tuple(int(num) for num in re.findall(r"\d+", lines[i]))
            a = Button(x, y)
            x, y = tuple(int(num) for num in re.findall(r"\d+", lines[i + 1]))
            b = Button(x, y)
            x, y = tuple(int(num) for num in re.findall(r"\d+", lines[i + 2]))
            p = (x, y)
            data.append((a, b, p))
        return data


def solve(machines):
    return sum([solve_machine(*machine) for machine in machines])


def solve_machine(a, b, p):
    X, Y = p
    min_cost = MAX
    for count_a in range(100, 0, -1):
        target_x = X - count_a * a.x
        target_y = Y - count_a * a.y
        div_x, mod_x = divmod(target_x, b.x)
        div_y, mod_y = divmod(target_y, b.y)
        if mod_x == mod_y == 0 and div_x == div_y:
            curr_cost = cost(count_a, div_x)
            if curr_cost < min_cost:
                min_cost = curr_cost
    return min_cost if min_cost != MAX else 0


def cost(a, b):
    return 3 * a + b


def main():
    machines = get_input("input.txt")
    print(solve(machines))


if __name__ == "__main__":
    main()
