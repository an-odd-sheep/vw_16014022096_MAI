class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dls(root, target, depth):
    if root is None or depth < 0:
        return None
    
    if root.value == target:
        return [root.value]
    
    left_path = dls(root.left, target, depth - 1)
    if left_path:
        return [root.value] + left_path
    
    right_path = dls(root.right, target, depth - 1)
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
depth_limit = int(input("Enter the depth limit: "))

path = dls(root, value, depth_limit)

if path:
    print("DLS traversal:", path)
else:
    print("Node not found in the tree within the specified depth limit.")
