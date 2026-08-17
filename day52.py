class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lca(root, a, b):
    if root is None:
        return None

    if root.val == a or root.val == b:
        return root

    left = lca(root.left, a, b)
    right = lca(root.right, a, b)

    if left is not None and right is not None:
        return root

    if left is not None:
        return left

    return right


n = int(input())
values = list(map(int, input().split()))
a, b = map(int, input().split())

if n == 0 or values[0] == -1:
    print(-1)
else:
    nodes = [None if x == -1 else TreeNode(x) for x in values]

    for i in range(n):
        if nodes[i] is not None:
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n:
                nodes[i].left = nodes[left]

            if right < n:
                nodes[i].right = nodes[right]

    answer = lca(nodes[0], a, b)
    print(answer.val if answer else -1)