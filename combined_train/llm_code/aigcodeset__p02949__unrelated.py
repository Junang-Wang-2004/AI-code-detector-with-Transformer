import sys
from collections import deque
v1, v2, v3 = map(int, sys.stdin.readline().split())
v4 = [[] for v5 in range(v1 + 1)]
for v5 in range(v2):
    v6, v7, v8 = map(int, sys.stdin.readline().split())
    v4[v6].append((v7, v8))
v9 = 10 ** 18
v10 = [v9] * (v1 + 1)
v10[1] = 0
v11 = deque([(1, 0)])
while v11:
    v12, v13 = v11.popleft()
    for v14, v15 in v4[v12]:
        if v10[v14] > v10[v12] + v15:
            v10[v14] = v10[v12] + v15
            v11.append((v14, v13 + 1))
v16 = -1
for v17 in range(1, v1 + 1):
    if v10[v17] != v9:
        v16 = max(v16, v10[v17] - v3 * (v10[v17] // v15) if (v14, v15) in v4[v17] else v10[v17])
print(v16)
