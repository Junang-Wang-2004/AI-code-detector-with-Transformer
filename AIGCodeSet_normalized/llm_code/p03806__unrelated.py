import sys
from collections import defaultdict
v1, v2, v3 = map(int, sys.stdin.readline().split())
v4 = []
for v5 in range(v1):
    v6, v7, v8 = map(int, sys.stdin.readline().split())
    v4.append((v6, v7, v8))
v9 = float('inf')
for v10 in range(1, 101):
    for v11 in range(1, 101):
        if v10 * v3 == v11 * v2:
            v12 = 0
            v13 = defaultdict(int)
            for v6, v7, v8 in v4:
                if v6 * v10 + v7 * v11 <= v10 * v3:
                    v13[v6, v7, v8] += 1
                    v12 += v13[v6, v7, v8] * v8
                    if v6 * v10 + v7 * v11 == v10 * v3:
                        if v12 < v9:
                            v9 = v12
                        break
            if v12 < v9:
                v9 = v12
if v9 == float('inf'):
    print(-1)
else:
    print(v9)
