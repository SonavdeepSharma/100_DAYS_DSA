n = int(input())
arr = list(map(int, input().split()))

arr.sort()

left = 0
right = n - 1

min_sum = float('inf')
x = y = 0

while left < right:
    s = arr[left] + arr[right]

    if abs(s) < min_sum:
        min_sum = abs(s)
        x = arr[left]
        y = arr[right]

    if s < 0:
        left += 1
    else:
        right -= 1

print(x, y)