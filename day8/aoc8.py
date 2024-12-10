def get_input(path):
    with open(path, "r") as file:
        grid = file.readlines()
        grid = [line.strip() for line in grid]
        return grid


def phase_1():
    types = get_node_types()
    get_node_positions(types)
    antinodes = get_antinodes(types)
    res = count_antinodes(antinodes)
    print(res)


def get_node_types():
    """
    return a dict types
    keys are types of nodes
    values are empty sets, will eventually contain location of nodes of that type
    """
    types = set()
    for row in grid:
        for elem in row:
            if elem != ".":
                types.add(elem)

    types = {tp: set() for tp in types}
    return types


def get_node_positions(types):
    """
    record the position of each node in the corresponding type bin
    """
    for x, row in enumerate(grid):
        for y, elem in enumerate(row):
            if elem != ".":
                types[elem].add((x, y))


def get_antinodes(types):
    """
    iterate through each node_type, each pair of distinct nodes of that type
    compute the corresponding antinode and add to antinode list
    """
    antinodes = set()
    for node_type in types.keys():
        # current_antinodes = set()
        for node_a in types[node_type]:
            for node_b in types[node_type]:
                if node_a is not node_b:
                    add_antinode(node_a, node_b, antinodes)
        # antinodes.append(current_antinodes)
    return antinodes


def add_antinode(node_a, node_b, antinode_set):
    """
    compute manhattan distance dist between a, b
    find point dist away from b
    if in bounds, add to antinodes
    """
    x, y = man_dist(node_a, node_b)
    antinode_pos = node_b[0] + x, node_b[1] + y
    if in_bounds(antinode_pos):
        antinode_set.add(antinode_pos)


def man_dist(node_a, node_b):
    x1, y1 = node_a
    x2, y2 = node_b
    return x2 - x1, y2 - y1


def in_bounds(node):
    x, y = node
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


def count_antinodes(antinodes):
    return len(antinodes)


if __name__ == "__main__":
    grid = get_input("input.txt")
    phase_1()

