counter = 0  

class tree:
    def __init__(self, value):
        self.val = value
        self.children = []

def bfs(root, search_value):
    global counter  
    if root is None:
        return None

    queue = [root]

    while queue:
        counter += 1  
        node = queue.pop(0)
        if search_value == node.val:
            return node.val

        for child in node.children:
            queue.append(child)

root = tree(1)
root.children = [tree(2), tree(3), tree(4)]
root.children[0].children = [tree(5), tree(6)]
root.children[2].children = [tree(7), tree(8)]

print("Implementing BFS for search tree")
search_value = int(input("Enter value you want to search for: "))

x = bfs(root, search_value)
print("Node found:", x)
print("Time Complexity:", counter)
