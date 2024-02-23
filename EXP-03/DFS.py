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


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

value = int(input("Enter the value of the node to find the path for: "))

path = dfs(root, value)
if path:
    print("DFS traversal:", path)
else:
    print("Node not found in the tree.")
