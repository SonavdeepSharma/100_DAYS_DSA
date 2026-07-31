n = int(input())
arr = list(map(int, input().split()))

queue = [0] * n
front = 0
rear = -1


for x in arr:
    rear += 1
    queue[rear] = x


for i in range(front, rear + 1):
    print(queue[i], end=" ")