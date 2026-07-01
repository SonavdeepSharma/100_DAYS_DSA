p = int(input())
log1 = list(map(int, input().split()))

q = int(input())
log2 = list(map(int, input().split()))

i = 0
j = 0
merged = []

while i < p and j < q:
    if log1[i] <= log2[j]:
        merged.append(log1[i])
        i += 1
    else:
        merged.append(log2[j])
        j += 1

while i < p:
    merged.append(log1[i])
    i += 1

while j < q:
    merged.append(log2[j])
    j += 1

print(*merged)