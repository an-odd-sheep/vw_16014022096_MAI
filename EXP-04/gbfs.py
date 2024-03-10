from queue import PriorityQueue

vertex = 14
graph = [[] for i in range(vertex)]

def best_first_search(start, end, vertex):
   
    visited = [False] * vertex
   
    pqueue = PriorityQueue()
    pqueue.put((0, start, [start]))
   
    visited[start] = True

    while pqueue.empty() == False:
        cost, current, path = pqueue.get()
       
        if current == end:
            return path, cost  
       
        for next_vertex, edge_cost in graph[current]:
            if visited[next_vertex] == False:
                visited[next_vertex] = True
                new_path = path + [next_vertex]
                new_cost = cost + edge_cost  
                pqueue.put((new_cost, next_vertex, new_path))  
   
    return None, None  

def create_graph(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))


create_graph(0, 1, 3)
create_graph(0, 2, 6)
create_graph(0, 3, 5)
create_graph(1, 4, 9)
create_graph(1, 5, 8)
create_graph(2, 6, 12)
create_graph(2, 7, 14)
create_graph(3, 8, 7)
create_graph(8, 9, 5)
create_graph(8, 10, 6)
create_graph(9, 11, 1)
create_graph(9, 12, 10)
create_graph(9, 13, 2)


source = 0
target = 11


path, cost = best_first_search(source, target, vertex)


if path is not None:
    print("Path:", path)
    print("Cost:", cost)
else:
    print("No path found from", source, "to", target)
