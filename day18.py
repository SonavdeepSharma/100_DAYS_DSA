n = int(input())
arr = list(map(int, input().split()))
k = int(input())

k %= n

rotated = arr[-k:] + arr[:-k]
print(*rotated)