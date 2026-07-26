class Node:
    def __init__(self, coeff, exp):
        self.coeff = coeff
        self.exp = exp
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, coeff, exp):
        new_node = Node(coeff, exp)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.coeff, end="")
            if temp.exp > 1:
                print(f"x^{temp.exp}", end="")
            elif temp.exp == 1:
                print("x", end="")

            if temp.next:
                print(" + ", end="")
            temp = temp.next


n = int(input())

ll = LinkedList()

for _ in range(n):
    coeff, exp = map(int, input().split())
    ll.insert(coeff, exp)

ll.display()