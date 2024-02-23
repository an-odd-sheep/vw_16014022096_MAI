class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def DFS(node, goal):
    if node is None:
        return False
    print(node.value)
    if node.value == goal:
        return True
    for child in node.children:
        if DFS(child, goal):
            return True
    return False

def DLS(node, goal, depth):
    if node is None or depth < 0:
        return False
    print(node.value)
    if node.value == goal:
        return True
    if depth == 0:
        return False
    for child in node.children:
        if DLS(child, goal, depth - 1):
            return True
    return False

def ID_DFS(node, goal):
    depth = 0
    while True:
        print("Depth Limit:", depth)
        if DLS(node, goal, depth):
            return True
        depth += 1

# Example Usage:
# Constructing a simple search tree
root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

root.add_child(node2)
root.add_child(node3)
node2.add_child(node4)
node3.add_child(node5)

print("DFS:")
DFS(root, 5)

print("\nDLS:")
DLS(root, 5, 3)  # Depth limit is 3

print("\nID-DFS:")
ID_DFS(root, 5)
