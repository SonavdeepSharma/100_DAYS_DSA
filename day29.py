class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def rotateRight(head, k):
    if head is None or head.next is None or k == 0:
        return head

   
    length = 1
    last = head
    while last.next:
        last = last.next
        length += 1

    
    k = k % length
    if k == 0:
        return head

    
    last.next = head

    
    steps = length - k
    new_last = head
    for _ in range(steps - 1):
        new_last = new_last.next

    
    new_head = new_last.next
    new_last.next = None

    return new_head



n = int(input())

values = list(map(int, input().split()))

k = int(input())


head = None
tail = None

for value in values:
    new_node = Node(value)
    if head is None:
        head = new_node
        tail = new_node
    else:
        tail.next = new_node
        tail = new_node


head = rotateRight(head, k)

temp = head
while temp:
    print(temp.data, end=" ")
    temp = temp.next