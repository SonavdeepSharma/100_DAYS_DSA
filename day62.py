n = int(input("Enter number of vertices: "))
m = int(input("Enter number of edges: "))

adj = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())

    
    adj[u].append(v)
    adj[v].append(u)

print("Adjacency List:")
for i in range(n):
    print(i, "->", adj[i])