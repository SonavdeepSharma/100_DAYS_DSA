n = int(input())

arr = list(map(int, input().split()))

key = int(input())

found = False

for i in range(len(arr)):
    if arr[i] == key and not found:
        arr.pop(i)
        found = True
        break

for num in arr:
    print(num, end=" ")