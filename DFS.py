# Implementing Depth First Search Algorithm
# Three types of DFS algorithms
# In order, Pre order, Post Order

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

def preorder(root):
    if root is None:
        return
    
    print(root.val, end = " ")
    preorder(root.left)
    preorder(root.right)

preorder(root)

def inorder(root):
    if root is None:
        return
    
    inorder(root.left)
    print(root.val, end = " ")
    inorder(root.right)

def postorder(root):
    if root is None:
        return
    
    inorder(root.left)
    inorder(root.right)
    print(root.val, end = " ")

    