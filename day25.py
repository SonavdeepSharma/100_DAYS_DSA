class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

n = int(input())
arr = list(map(int, input().split()))
key = int(input())

head = None
temp = None

for value in arr:
    newNode = Node(value)

    if head is None:
        head = newNode
        temp = newNode
    else:
        temp.next = newNode
        temp = newNode

count = 0
temp = head

while temp is not None:
    if temp.data == key:
        count += 1
    temp = temp.next

print(count)