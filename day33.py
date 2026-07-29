exp = input()

stack = []
postfix = ""

priority = {'+':1, '-':1, '*':2, '/':2, '^':3}

for ch in exp:
    if ch.isalnum():
        postfix += ch
    elif ch == '(':
        stack.append(ch)
    elif ch == ')':
        while stack and stack[-1] != '(':
            postfix += stack.pop()
        stack.pop()
    else:
        while stack and stack[-1] != '(' and priority[stack[-1]] >= priority[ch]:
            postfix += stack.pop()
        stack.append(ch)

while stack:
    postfix += stack.pop()

print(postfix)