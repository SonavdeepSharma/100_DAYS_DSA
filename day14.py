n = int(input())

is_identity = True

for i in range(n):
    row = list(map(int, input().split()))

    for j in range(n):
        if i == j:
            if row[j] != 1:
                is_identity = False
        else:
            if row[j] != 0:
                is_identity = False

if is_identity:
    print("Identity Matrix")
else:
    print("Not an Identity Matrix")