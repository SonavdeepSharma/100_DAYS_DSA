n = int(input())

queue = list(map(int, input().split()))

m = int(input())

for i in range(m):
    x = queue.pop(0)   # Dequeue from front
    queue.append(x)    # Enqueue at rear (circular)

print(*queue)