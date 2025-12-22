class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return TreeNode(value)
    
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)


    return root

def delete(root, value):
    if root is None:
        return root
    
    if value < root.value:
        root.left = delete(root.left, value)
    elif value > root.value:
        root.right = delete(root.right, value)
    else:
        if root.left is None and root.right is None:
            return None
        
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        

        successor = find_min(root.right)
        root.value = successor.value
        root.right = delete(root.right, successor.value)


    return root

def find_min(node):
    while node.left:
        node = node.left
    return node

