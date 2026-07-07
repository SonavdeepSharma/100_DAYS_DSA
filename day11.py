m, n = map(int, input().split())

matrix1 = []
for i in range(m):
    matrix1.append(list(map(int, input().split())))

matrix2 = []
for i in range(m):
    matrix2.append(list(map(int, input().split())))

for i in range(m):
    for j in range(n):
        print(matrix1[i][j] + matrix2[i][j], end=" ")
    print()