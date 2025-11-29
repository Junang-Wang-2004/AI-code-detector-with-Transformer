import sys
from collections import deque
v1, v2 = map(int, sys.stdin.readline().split())
v3 = [[] for v4 in range(v1)]
v5 = [0] * v1
for v4 in range(v2):
    v6, v7 = map(int, sys.stdin.readline().split())
    v3[v6 - 1].append(v7 - 1)
    v5[v7 - 1] += 1
v8 = deque([i for v9 in range(v1) if v5[v9] == 0])
v10 = [0] * v1
while v8:
    v6 = v8.popleft()
    for v7 in v3[v6]:
        v5[v7] -= 1
        v10[v7] = max(v10[v7], v10[v6] + 1)
        if v5[v7] == 0:
            v8.append(v7)
print(max(v10))
