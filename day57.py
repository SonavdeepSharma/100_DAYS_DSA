n = int(input())
a = list(map(int, input().split()))


for i in range(n):
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and right < n:
        a[left], a[right] = a[right], a[left]


stack = []
i = 0

while stack or i < n:
    while i < n and a[i] != -1:
        stack.append(i)
        i = 2 * i + 1

    if stack:
        i = stack.pop()
        print(a[i], end=" ")
        i = 2 * i + 2