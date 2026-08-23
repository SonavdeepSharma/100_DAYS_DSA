class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root = Node(preorder[0])

    mid = inorder.index(preorder[0])

    root.left = build_tree(
        preorder[1:mid + 1],
        inorder[:mid]
    )

    root.right = build_tree(
        preorder[mid + 1:],
        inorder[mid + 1:]
    )

    return root


def postorder(root):
    if root is None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.value, end=" ")


n = int(input())

preorder = list(map(int, input().split()))
inorder = list(map(int, input().split()))

root = build_tree(preorder, inorder)

postorder(root)