n = int(input())
tree = list(map(int, input().split()))

count = 0

for i in range(n):
    if tree[i] == -1:
        continue

    left = 2 * i + 1
    right = 2 * i + 2

    left_missing = left >= n or tree[left] == -1
    right_missing = right >= n or tree[right] == -1

    if left_missing and right_missing:
        count += 1

print(count)