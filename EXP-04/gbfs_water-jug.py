from queue import PriorityQueue

def best_first_search(start, end, graph):
    visited = [False] * len(graph)
    pqueue = PriorityQueue()
    pqueue.put((0, start, [start]))
    visited[start] = True

    while not pqueue.empty():
        cost, current, path = pqueue.get()

        if current == end:
            return path, cost

        for next_vertex, edge_cost in graph[current]:
            if not visited[next_vertex[0]]:
                visited[next_vertex[0]] = True
                new_path = path + [next_vertex[0]]
                new_cost = cost + edge_cost
                pqueue.put((new_cost, next_vertex[0], new_path))

    return None, None

def water_jug_graph(max_jug1, max_jug2):
    graph = [[] for _ in range((max_jug1 + 1) * (max_jug2 + 1))]

    for i in range(max_jug1 + 1):
        for j in range(max_jug2 + 1):
            # Fill jug 1
            graph[i * (max_jug2 + 1) + j].append(((max_jug1, j), 1))
            # Fill jug 2
            graph[i * (max_jug2 + 1) + j].append(((i, max_jug2), 1))
            # Empty jug 1
            graph[i * (max_jug2 + 1) + j].append(((0, j), 1))
            # Empty jug 2
            graph[i * (max_jug2 + 1) + j].append(((i, 0), 1))
            # Pour from jug 1 to jug 2
            pour = min(i, max_jug2 - j)
            graph[i * (max_jug2 + 1) + j].append(((i - pour, j + pour), 1))
            # Pour from jug 2 to jug 1
            pour = min(j, max_jug1 - i)
            graph[i * (max_jug2 + 1) + j].append(((i + pour, j - pour), 1))

    return graph

def solve_water_jug(max_jug1, max_jug2, target):
    graph = water_jug_graph(max_jug1, max_jug2)
    source = 0
    target_index = target[0] * (max_jug2 + 1) + target[1]
    path, cost = best_first_search(source, target_index, graph)

    if path is not None:
        print("Path:")
        for state in path:
            jug1 = state // (max_jug2 + 1)
            jug2 = state % (max_jug2 + 1)
            print("Jug 1:", jug1, "Jug 2:", jug2)
        print("Cost:", cost)
    else:
        print("No solution found.")

# Example usage
max_jug1 = 4
max_jug2 = 3
target = (2, 0)  # Target state, where jug 1 has 2 units and jug 2 has 0 units
solve_water_jug(max_jug1, max_jug2, target)
