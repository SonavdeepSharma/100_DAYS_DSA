import heapq

n = int(input())
heap = []

for _ in range(n):
    op = input().split()

    if op[0] == "insert":
        heapq.heappush(heap, int(op[1]))

    elif op[0] == "extractMin":
        if heap:
            print(heapq.heappop(heap))
        else:
            print(-1)

    elif op[0] == "peek":
        if heap:
            print(heap[0])
        else:
            print(-1)