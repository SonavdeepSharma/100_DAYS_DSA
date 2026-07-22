n = int(input())
arr = list(map(int, input().split()))

head = None
tail = None

for x in arr:
    node = [x, None, None]   

    if head is None:
        head = node
        tail = node
    else:
        tail[2] = node
        node[1] = tail
        tail = node

temp = head
while temp:
    print(temp[0], end=" ")
    temp = temp[2]