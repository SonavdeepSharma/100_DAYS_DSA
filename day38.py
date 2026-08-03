from collections import deque

dq = deque()


dq.appendleft(10)   
dq.append(20)       
dq.appendleft(5)
dq.append(30)

print("Deque:", list(dq))


print("Front:", dq[0])
print("Back:", dq[-1])


dq.popleft()        
dq.pop()            

print("After Pop:", list(dq))


print("Size:", len(dq))


print("Is Empty?", len(dq) == 0)

dq.reverse()
print("Reversed:", list(dq))

temp = sorted(dq)
dq = deque(temp)
print("Sorted:", list(dq))


dq.clear()
print("After Clear:", list(dq))
print("Is Empty?", len(dq) == 0)