m, n = map(int, input("Enter number of rows and columns: ").split())

matrix = []

print("Enter the matrix elements:")
for i in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)

if m != n:
    print("Not a Symmetric Matrix")
else:
    symmetric = True
    for i in range(m):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                symmetric = False
                break
        if not symmetric:
            break

    if symmetric:
        print("Symmetric Matrix")
    else:
        print("Not a Symmetric Matrix")