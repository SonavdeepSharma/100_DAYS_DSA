from collections import deque

n = int(input())
arr = list(map(int, input().split()))

if n == 0:
    print()
else:
    root = arr[0]
    queue = deque([(0, 0)])
    ans = []

    while queue:
        idx, level = queue.popleft()

        if len(ans) == level:
            ans.append(arr[idx])

        if 2 * idx + 2 < n and arr[2 * idx + 2] != -1:
            queue.append((2 * idx + 2, level + 1))

        if 2 * idx + 1 < n and arr[2 * idx + 1] != -1:
            queue.append((2 * idx + 1, level + 1))

    print(*ans)