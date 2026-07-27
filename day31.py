stack = []

n = int(input())

for _ in range(n):
    operation = list(map(int, input().split()))

    if operation[0] == 1:
        stack.append(operation[1])

    elif operation[0] == 2:
        if len(stack) == 0:
            print("Stack Underflow")
        else:
            print(stack.pop())

    elif operation[0] == 3:
        if len(stack) == 0:
            print("Stack is Empty")
        else:
            for i in range(len(stack) - 1, -1, -1):
                print(stack[i], end=" ")
            print()