class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

head1 = None
tail1 = None

for x in a:
    node = Node(x)
    if head1 is None:
        head1 = node
        tail1 = node
    else:
        tail1.next = node
        tail1 = node

head2 = None
tail2 = None

common = {}

for x in b:
    if x in common:
        node = common[x]
    else:
        node = Node(x)
        common[x] = node

    if head2 is None:
        head2 = node
        tail2 = node
    else:
        tail2.next = node
        tail2 = node

temp = head1
while temp:
    common[temp.data] = temp
    temp = temp.next

temp = head2
while temp:
    if temp.data in common and common[temp.data] is not temp:
        print(temp.data)
        break
    temp = temp.next
else:
    print("No Intersection")