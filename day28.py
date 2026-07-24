class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


n = int(input())
arr = list(map(int, input().split()))

head = None
tail = None

# Create Circular Linked List
for x in arr:
    new_node = Node(x)
    if head is None:
        head = new_node
        tail = new_node
    else:
        tail.next = new_node
        tail = new_node

# Make it circular
tail.next = head

# Traverse and print
temp = head
while True:
    print(temp.data, end=" ")
    temp = temp.next
    if temp == head:
        break