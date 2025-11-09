class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def insert(root, key):
    # The only change is on this line: 'in' is replaced with 'is'
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" / ")
        inorder_traversal(root.right)

# --- Your test code (which is perfect) ---
root = None
root = insert(root, 20)
root = insert(root, 30)
root = insert(root, 10)

print("Inorder traversal:")
inorder_traversal(root)