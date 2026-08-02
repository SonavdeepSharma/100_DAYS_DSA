n = int(input())

pq = []

for _ in range(n):
    op = input().split()

    if op[0] == "insert":
        pq.append(int(op[1]))
        pq.sort()

    elif op[0] == "delete":
        if len(pq) == 0:
            print(-1)
        else:
            print(pq.pop(0))

    elif op[0] == "peek":
        if len(pq) == 0:
            print(-1)
        else:
            print(pq[0])