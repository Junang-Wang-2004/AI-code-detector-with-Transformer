v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
from collections import deque
v3 = deque(v3)
import copy
v4 = -10 ** 18
for v5 in range(v2 + 1):
    for v6 in range(v2 + 1):
        if v5 + v6 > v2:
            continue
        if v5 + v6 < v2 - (v5 + v6):
            continue
        if v5 + v6 > v1:
            continue
        v7 = copy.copy(v3)
        v8 = []
        for v9 in range(v5):
            v8.append(v7.popleft())
        for v10 in range(v6):
            v8.append(v7.pop())
        v8.sort()
        v11 = sum(v8)
        v12 = v2 - v5 - v6
        for v13 in range(v12):
            if v8[v13] < 0:
                v11 -= v8[v13]
        v4 = max(v4, v11)
print(v4)
