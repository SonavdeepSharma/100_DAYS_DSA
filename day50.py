n = int(input())
tree = list(map(int, input().split()))
val = int(input())

i = 0

while i < n and tree[i] != -1:
    if tree[i] == val:
        print("true")
        break
    elif val < tree[i]:
        i = 2 * i + 1
    else:
        i = 2 * i + 2
else:
    print("false")