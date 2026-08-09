class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


def preorder(root):
    if root is None:
        return

    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)


def postorder(root):
    if root is None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")


n = int(input())
arr = list(map(int, input().split()))

if n == 0:
    exit()

nodes = []

for value in arr:
    if value == -1:
        nodes.append(None)
    else:
        nodes.append(Node(value))

for i in range(n):
    if nodes[i] is not None:
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n:
            nodes[i].left = nodes[left]

        if right < n:
            nodes[i].right = nodes[right]

root = nodes[0]

inorder(root)
print()

preorder(root)
print()

postorder(root)
print()