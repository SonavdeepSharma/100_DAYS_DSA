from collections import deque

n = int(input())
arr = list(map(int, input().split()))

if n == 0:
    print([])
else:
    root = arr[0]
    q = deque([0])
    ans = []
    left_to_right = True

    while q:
        level = []

        for _ in range(len(q)):
            i = q.popleft()

            if arr[i] != -1:
                level.append(arr[i])

                left = 2 * i + 1
                right = 2 * i + 2

                if left < n and arr[left] != -1:
                    q.append(left)

                if right < n and arr[right] != -1:
                    q.append(right)

        if not left_to_right:
            level.reverse()

        ans += level
        left_to_right = not left_to_right

    print(*ans)