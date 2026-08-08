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


n = int(input())
a = list(map(int, input().split()))

nodes = []

for x in a:
    if x == -1:
        nodes.append(None)
    else:
        nodes.append(Node(x))

for i in range(n):
    if nodes[i]:
        if 2 * i + 1 < n:
            nodes[i].left = nodes[2 * i + 1]

        if 2 * i + 2 < n:
            nodes[i].right = nodes[2 * i + 2]

inorder(nodes[0])