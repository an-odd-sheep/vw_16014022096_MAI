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