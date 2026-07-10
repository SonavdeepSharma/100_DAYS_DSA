r, c = map(int, input("Enter rows and columns: ").split())

matrix = []
print("Enter the matrix:")
for i in range(r):
    matrix.append(list(map(int, input().split())))

top = 0
bottom = r - 1
left = 0
right = c - 1

while top <= bottom and left <= right:
    for i in range(left, right + 1):
        print(matrix[top][i], end=" ")
    top += 1

    for i in range(top, bottom + 1):
        print(matrix[i][right], end=" ")
    right -= 1

    if top <= bottom:
        for i in range(right, left - 1, -1):
            print(matrix[bottom][i], end=" ")
        bottom -= 1

    if left <= right:
        for i in range(bottom, top - 1, -1):
            print(matrix[i][left], end=" ")
        left += 1