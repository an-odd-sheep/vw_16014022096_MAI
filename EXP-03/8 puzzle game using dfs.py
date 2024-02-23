class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def get_neighbors(state):
    neighbors = []
    zero_index = state.index(0)
    if zero_index >= 3:
        new_state = state.copy()  
        new_state[zero_index], new_state[zero_index - 3] = new_state[zero_index - 3], new_state[zero_index] 
        neighbors.append(new_state)
    if zero_index < 6:
        new_state = state.copy()
        new_state[zero_index], new_state[zero_index + 3] = new_state[zero_index + 3], new_state[zero_index]  
        neighbors.append(new_state)
    if zero_index % 3 != 0:
        new_state = state.copy()
        new_state[zero_index], new_state[zero_index - 1] = new_state[zero_index - 1], new_state[zero_index] 
        neighbors.append(new_state)
    if (zero_index + 1) % 3 != 0:
        new_state = state.copy()
        new_state[zero_index], new_state[zero_index + 1] = new_state[zero_index + 1], new_state[zero_index]  
        neighbors.append(new_state)
    return neighbors

def dfs(initial_state, final_state):
    visited = set()
    stack = [(initial_state, [])]

    while stack:
        state, path = stack.pop()
        visited.add(tuple(state))

        if state == final_state:
            return path

        for neighbor in get_neighbors(state):
            if tuple(neighbor) not in visited:
                stack.append((neighbor, path + [neighbor]))

    return None



print("Enter initial state of the puzzle (0 represents the empty tile):")
initial_state = [int(input()) for _ in range(9)]
print("Enter final state of the puzzle:")
final_state = [int(input()) for _ in range(9)]

path = dfs(initial_state, final_state)

if path:
    print("Shortest path to reach the final state:")
    step = 1
    for state in path:
        print("Step", step)
        print(state[:3])
        print(state[3:6])
        print(state[6:])
        print()
        step += 1
else:
    print("No solution exists for the given states.")



