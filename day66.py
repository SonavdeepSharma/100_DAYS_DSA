def has_cycle(V, edges):
    graph = [[] for _ in range(V)]

    for u, v in edges:
        graph[u].append(v)

    visited = [False] * V
    path = [False] * V

    def dfs(node):
        visited[node] = True
        path[node] = True

        for nei in graph[node]:
            if not visited[nei]:
                if dfs(nei):
                    return True
            elif path[nei]:
                return True

        path[node] = False
        return False

    for i in range(V):
        if not visited[i]:
            if dfs(i):
                return "YES"

    return "NO"


V, E = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(E)]

print(has_cycle(V, edges))