v1 = input()
from collections import deque
v2 = deque(v1)
v3 = 0
while len(v2) > 1:
    if v2[0] == v2[-1]:
        v2.popleft()
        v2.pop()
    elif v2[0] == 'x':
        v3 += 1
        v2.append('x')
    elif v2[-1] == 'x':
        v3 += 1
        v2.appendleft('x')
    if 'x' not in v2:
        break
if len(v2) == 1:
    print(v3)
else:
    print(-1)
