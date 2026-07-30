stack = []

exp = input().split()

for x in exp:
    if x.lstrip("-").isdigit():
        stack.append(int(x))
    else:
        b = stack.pop()
        a = stack.pop()

        if x == "+":
            stack.append(a + b)
        elif x == "-":
            stack.append(a - b)
        elif x == "*":
            stack.append(a * b)
        elif x == "/":
            stack.append(int(a / b))

print(stack.pop())