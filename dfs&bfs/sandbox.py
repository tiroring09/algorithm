from collections import deque

dq = deque()
dq.append(1)
while dq:
    print(dq)
    dq.pop()