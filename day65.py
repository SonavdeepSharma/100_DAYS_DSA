from collections import defaultdict

def has_cycle(V, edges):
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * V

    def dfs(node, parent):
        visited[node] = True

        for nei in graph[node]:
            if not visited[nei]:
                if dfs(nei, node):
                    return True
            elif nei != parent:
                return True

        return False

    for i in range(V):
        if not visited[i]:
            if dfs(i, -1):
                return "YES"

    return "NO"

V, E = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(E)]

print(has_cycle(V, edges))