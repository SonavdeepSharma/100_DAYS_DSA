n = int(input("Enter array size: "))

print("Enter array elements:")
arr = list(map(int, input().split()))

k = int(input("Enter key to search: "))

comparisons = 0
found = False

for i in range(n):
    comparisons += 1
    if arr[i] == k:
        print("Found at index", i)
        found = True
        break

if not found:
    print("Not Found")

print("Comparisons =", comparisons)