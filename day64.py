from collections import deque

n = int(input())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

s = int(input())

visited = [False] * n
q = deque()

q.append(s)
visited[s] = True

result = []

while q:
    u = q.popleft()
    result.append(u)

    for v in graph[u]:
        if not visited[v]:
            visited[v] = True
            q.append(v)

print(*result)