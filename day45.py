n = int(input())
tree = list(map(int, input().split()))

for i in range(n):
    if tree[i] != -1:
        print(tree[i], end=" ")