n = int(input())

arr = list(map(int, input().split()))

pos = int(input())

for i in range(pos - 1, n - 1):
    arr[i] = arr[i + 1]


for i in range(n - 1):
    print(arr[i], end=" ")