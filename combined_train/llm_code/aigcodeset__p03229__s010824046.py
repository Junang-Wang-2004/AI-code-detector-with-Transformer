v1 = int(input())
v2 = [int(input()) for v3 in range(v1)]
from collections import deque
v4 = deque(sorted(v2))
v5 = deque([v4.pop()])
while v4:
    v5.appendleft(v4.pop())
    if len(v4) == 0:
        break
    v5.append(v4.popleft())
    if len(v4) == 0:
        break
    v5.appendleft(v4.pop())
    if len(v4) == 0:
        break
    v5.append(v4.popleft())
    if len(v4) == 0:
        break
v6 = v5.popleft()
v7 = 0
while v5:
    v7 += abs(v6 - v5[0])
    v6 = v5.popleft()
print(v7)
