def get_input(path):
    with open(path, "r") as file:
        grid = file.readlines()
        grid = [line.strip() for line in grid]
        return grid


def get_adjacency_list(grid):
    adjacency_list = set()
    height, width = len(grid), len(grid[0])
    for x, row in enumerate(grid):
        for y, elem in enumerate(row):
            if x < height - 1 and elem == grid[x + 1][y]:
                edge = Edge((x, y), (x + 1, y))
                adjacency_list.add(edge)
            if y < width - 1 and elem == grid[x][y + 1]:
                edge = Edge((x, y), (x, y + 1))
                adjacency_list.add(edge)
    return adjacency_list


def get_nodes(grid):
    return [(x, y) for y in range(len(grid[0])) for x in range(len(grid))]


class Edge:
    def __init__(self, node_a, node_b):
        self.node_a = node_a
        self.node_b = node_b


class Graph:
    def __init__(self, nodes, edges):
        self.edges = edges
        self.nodes = nodes

    def get_neighbors(self, node):
        neighbors = set()
        for edge in self.edges:
            if node == edge.node_a:
                neighbors.add(edge.node_b)
            if node == edge.node_b:
                neighbors.add(edge.node_a)
        return neighbors


class Component:
    def __init__(self, nodes, degrees):
        self.nodes = nodes
        self.degrees = degrees
        self.size = len(nodes)


def phase1():
    components = connected_components(graph)
    cost = sum(map(component_cost, components))
    print(f"Phase 1: {cost}")


def connected_components(graph):
    components = []
    seen = {node: False for node in graph.nodes}
    for node in graph.nodes:
        if not seen[node]:
            component = get_component(node, graph)
            for new_node in component.nodes:
                seen[new_node] = True
            components.append(component.degrees)
    return components


def get_component(node, graph):
    degrees = []
    component = {node}
    queue = [node]
    while queue:
        curr_node = queue.pop(0)
        deg = 0
        neighbors = graph.get_neighbors(curr_node)
        for neighbor in neighbors:
            deg += 1
            if neighbor not in component:
                component.add(neighbor)
                queue.append(neighbor)
        degrees.append(deg)
    return Component(component, degrees)


def component_cost(degrees):
    cost = area(degrees) * perimeter(degrees)
    return cost


def area(degrees):
    return len(degrees)


def perimeter(degrees):
    return sum(map(lambda x: 4 - x, degrees))


if __name__ == "__main__":
    grid = get_input("input.txt")
    edges = get_adjacency_list(grid)
    nodes = get_nodes(grid)
    graph = Graph(nodes, edges)
    phase1()
