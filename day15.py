m, n = map(int, input().split())

sum_diagonal = 0

for i in range(m):
    row = list(map(int, input().split()))
    if i < n:
        sum_diagonal += row[i]

print(sum_diagonal) 