class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs(root, target):
    if root is None:
        return None
    
    if root.value == target:
        return [root.value]
    
    left_path = dfs(root.left, target)
    if left_path:
        return [root.value] + left_path
    
    right_path = dfs(root.right, target)
    if right_path:
        return [root.value] + right_path
    
    return None

def id_dfs_l(root, target):
    depth = 0
    while True:
        path = dfs(root, target)
        if path:
            return path
        depth += 1

def id_dfs_nl(root, target):
    depth = 1
    while True:
        path = dfs(root, target)
        if path:
            return path
        
        depth *= 2 


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

value = int(input("Enter the value of the node to find the path for: "))

path_l = id_dfs_l(root, value)
if path_l:
    print("ID-DFS traversal (increasing linearly):", path_l)
else:
    print("Node not found in the tree.")

path_nl = id_dfs_nl(root, value)  
if path_nl:
    print("ID-DFS traversal (increasing non-linearly):", path_nl)
else:
    print("Node not found in the tree.")
