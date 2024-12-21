class Edge:
    def __init__(self, node_a, node_b):
        self.node_a = node_a
        self.node_b = node_b


class Node:
    def __init__(self, pos, val):
        self.pos = pos
        self.val = val


def get_component(node, graph):
    queue = [node]
    component_edges = set()
    seen = {node}
    while queue:
        curr_node = queue.pop(0)
        for neighbor in graph.get_neighbors(curr_node):
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
                component_edges.add(Edge(curr_node, neighbor))
    return component_edges
