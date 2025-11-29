from pprint import pprint
from collections import deque
import sys
v1, v2 = map(int, sys.stdin.readline().strip().split(' '))
v3 = [[] for v4 in range(v1)]
for v4 in range(v1 - 1):
    v5, v6 = map(int, sys.stdin.readline().strip().split(' '))
    v3[v5 - 1].append(v6 - 1)
    v3[v6 - 1].append(v5 - 1)
v7 = [0] * v1
v8 = [0] * v1
for v4 in range(v2):
    v9, v10 = map(int, sys.stdin.readline().strip().split(' '))
    v7[v9 - 1] += v10
v11 = deque()
v11.append(0)
v12 = set()
while v11:
    v13 = v11.popleft()
    if v13 in v12:
        continue
    v12.add(v13)
    for v14 in v3[v13]:
        if v14 in v12:
            continue
        v7[v14] += v7[v13]
        v11.append(v14)
print(' '.join(list(map(str, v7))))
