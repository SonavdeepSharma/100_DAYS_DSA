n = int(input())
arr = list(map(int, input().split()))

if n == 0:
    print("YES")
else:
    symmetric = True

    
    queue = [(1, 2)]

    while queue and symmetric:
        left, right = queue.pop(0)

        if left >= n or right >= n:
            continue

        if arr[left] == -1 and arr[right] == -1:
            continue

        if arr[left] == -1 or arr[right] == -1:
            symmetric = False
            break

        if arr[left] != arr[right]:
            symmetric = False
            break

        
        queue.append((2 * left + 1, 2 * right + 2))
        queue.append((2 * left + 2, 2 * right + 1))

    if symmetric:
        print("YES")
    else:
        print("NO")