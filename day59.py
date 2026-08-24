n = int(input())

inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))


pos = {}
for i in range(n):
    pos[inorder[i]] = i


left = [-1] * n
right = [-1] * n

node = {}

for i in range(n):
    node[inorder[i]] = i

post_index = n - 1


stack = [(0, n - 1, -1, 0)]

root = -1

while stack:
    l, r, parent, side = stack.pop()

    if l > r:
        continue

    value = postorder[post_index]
    post_index -= 1

    curr = node[value]

    if parent == -1:
        root = curr
    elif side == 0:
        left[parent] = curr
    else:
        right[parent] = curr

    mid = pos[value]

   
    stack.append((l, mid - 1, curr, 0))
    stack.append((mid + 1, r, curr, 1))


stack = [root]

while stack:
    curr = stack.pop()

    if curr == -1:
        continue

    print(inorder[curr], end=" ")

   
    if right[curr] != -1:
        stack.append(right[curr])

    if left[curr] != -1:
        stack.append(left[curr])