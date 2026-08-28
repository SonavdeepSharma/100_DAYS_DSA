def dfs(graph, v, visited, result):
    visited[v] = True
    result.append(v)

    for nei in graph[v]:
        if not visited[nei]:
            dfs(graph, nei, visited, result)


n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

s = int(input())

visited = [False] * n
result = []

dfs(graph, s, visited, result)

print(*result)