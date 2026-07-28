n = int(input())

stack = list(map(int, input().split()))

m = int(input())

for _ in range(m):
    if stack:
        stack.pop()

while stack:
    print(stack.pop(), end=" ")