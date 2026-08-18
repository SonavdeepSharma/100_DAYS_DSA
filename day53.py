from collections import deque

n = int(input())
arr = list(map(int, input().split()))

if n == 0:
    exit()

queue = deque()
queue.append((0, 0))  

vertical = {}

while queue:
    index, hd = queue.popleft()

    if index >= n or arr[index] == -1:
        continue

    if hd not in vertical:
        vertical[hd] = []

    vertical[hd].append(arr[index])

    
    queue.append((2 * index + 1, hd - 1))

    
    queue.append((2 * index + 2, hd + 1))

for hd in sorted(vertical):
    print(*vertical[hd])