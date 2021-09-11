from collections import deque

q = deque()
q.append(5)
q.append(9)
q.append(2)
q.append(5)

print(q)

x = q.popleft()
print(x)
q.pop()
print(q)
