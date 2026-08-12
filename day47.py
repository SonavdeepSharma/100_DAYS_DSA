n = int(input())
tree = list(map(int, input().split()))

if n == 0 or tree[0] == -1:
    print(0)
else:
    height = 0
    level = [0]

    while level:
        height += 1
        next_level = []

        for i in level:
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and tree[left] != -1:
                next_level.append(left)

            if right < n and tree[right] != -1:
                next_level.append(right)

        level = next_level

    print(height)