from collections import deque

n = int(input())
q = deque(map(int, input().split()))

stack = []


while q:
    stack.append(q.popleft())

while stack:
    q.append(stack.pop())

print(*q)