from collections import namedtuple

Tribe = namedtuple('Tribe', ['boys', 'girls'])


def get_edge_list_from_stdin():
    edge_list = []
    edge_count = int(input())
    for i in range(edge_count):
        edge = list(map(int, input().split()))
        edge_list.append(edge)
    return edge_list


def get_adjacency_list_from_edge_list(edge_list):
    adjacency_list = {}
    for edge in edge_list:
        vertex1 = edge[0]
        vertex2 = edge[1]
        if vertex1 not in adjacency_list:
            adjacency_list[vertex1] = []
        if vertex2 not in adjacency_list:
            adjacency_list[vertex2] = []
        adjacency_list[vertex1].append(vertex2)
        adjacency_list[vertex2].append(vertex1)
    return adjacency_list


def explore_tribe(graph, start_vertex, visited):
    vertices_stack = [start_vertex]
    boys_count = 0
    girls_count = 0
    while vertices_stack:
        vertex = vertices_stack.pop()
        if not visited[vertex]:
            visited[vertex] = True
            if vertex % 2 == 0:
                girls_count += 1
            else:
                boys_count += 1

        for neighbour in graph[vertex]:
            if not visited[neighbour]:
                vertices_stack.append(neighbour)
    return Tribe(boys_count, girls_count)


def partition_by_tribe(graph):
    visited = {vertex: False for vertex in graph}
    tribes = []
    for vertex in graph:
        if not visited[vertex]:
            tribes.append(explore_tribe(graph, vertex, visited))
    return tribes


def count_pairs(tribes):
    girls_count = 0
    boys_count = 0
    impossible_pairs = 0
    for i, tribe in enumerate(tribes):
        girls_count += tribe.girls
        boys_count += tribe.boys
        impossible_pairs += tribe.girls * tribe.boys
    pairs_count = girls_count * boys_count - impossible_pairs
    return pairs_count


def wedd(edge_list):
    adjacency_list = get_adjacency_list_from_edge_list(edge_list)
    tribes = partition_by_tribe(adjacency_list)
    number_of_possible_pairs = count_pairs(tribes)
    return number_of_possible_pairs

if __name__ == '__main__':
    edge_list = get_edge_list_from_stdin()
    print(wedd(edge_list))
