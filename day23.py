n = int(input())
list1 = list(map(int, input().split()))

m = int(input())
list2 = list(map(int, input().split()))

i = 0
j = 0

while i < n and j < m:
    if list1[i] <= list2[j]:
        print(list1[i], end=" ")
        i += 1
    else:
        print(list2[j], end=" ")
        j += 1

while i < n:
    print(list1[i], end=" ")
    i += 1

while j < m:
    print(list2[j], end=" ")
    j += 1