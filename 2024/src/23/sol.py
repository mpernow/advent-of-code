import pathlib
from collections import defaultdict
from itertools import combinations

INPUT_PATH = pathlib.Path(__file__).parent.parent.parent / "input"

def get_input():
    connections = open(INPUT_PATH / "23").read().splitlines()
    connections = list(map(lambda c: (c.split("-")[0], c.split("-")[1]), connections))
    return connections

def build_connections_dict(connections):
    graph = defaultdict(set)
    for a, b in connections:
        graph[a].add(b)
        graph[b].add(a)
    graph = dict(graph)
    return graph

def get_triplets(graph):
    components = set()
    for node_a, neighbours in graph.items():
        for node_b, node_c in combinations(neighbours, 2):
            if node_b in graph[node_c]:
                components.add(tuple(sorted([node_a, node_b, node_c])))
    return components


def part1():
    connections = get_input()
    graph = build_connections_dict(connections)
    triplets = get_triplets(graph)
    print(sum(any(elem.startswith("t") for elem in component) for component in triplets))

def part2():
    connections = get_input()
    graph = build_connections_dict(connections)

    # Start from triplets and iteratively build larger
    components = get_triplets(graph)
    while len(components) > 1:
        components_new = set()
        for component in components:
            first, *others = component
            for neighbour in graph[first]:
                if all(neighbour in graph[other] for other in others):
                    components_new.add(tuple(sorted(component + (neighbour, ))))
                    break
        components=components_new
    biggest_component = next(iter(components))
    print(",".join(sorted(biggest_component)))

if __name__ == "__main__":
    part1()
    part2()