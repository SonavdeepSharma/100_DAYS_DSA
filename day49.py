n = int(input())
a = list(map(int, input().split()))
x = int(input())

a.append(x)


bst = []

for value in a:
    if not bst:
        bst.append(value)
    else:
        i = 0
        while True:
            if value < bst[i]:
                left = 2 * i + 1
                if left >= len(bst):
                    bst.extend([None] * (left - len(bst) + 1))
                if bst[left] is None:
                    bst[left] = value
                    break
                i = left
            else:
                right = 2 * i + 2
                if right >= len(bst):
                    bst.extend([None] * (right - len(bst) + 1))
                if bst[right] is None:
                    bst[right] = value
                    break
                i = right

result = []

def inorder(i):
    if i >= len(bst) or bst[i] is None:
        return
    inorder(2 * i + 1)
    result.append(bst[i])
    inorder(2 * i + 2)

inorder(0)

print(*result)