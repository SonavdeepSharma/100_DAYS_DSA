n = int(input())
arr = list(map(int, input().split()))

head = None
tail = None

for x in arr:
    node = {"data": x, "next": None}

    if head is None:
        head = node
        tail = node
    else:
        tail["next"] = node
        tail = node

temp = head

while temp is not None:
    print(temp["data"], end=" ")
    temp = temp["next"]