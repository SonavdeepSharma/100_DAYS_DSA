n = int(input())
arr = list(map(int, input().split()))
p, q = map(int, input().split())


root = None

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return Node(val)

    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)

    return root

for val in arr:
    root = insert(root, val)


while root:
    if p < root.val and q < root.val:
        root = root.left
    elif p > root.val and q > root.val:
        root = root.right
    else:
        print(root.val)
        break