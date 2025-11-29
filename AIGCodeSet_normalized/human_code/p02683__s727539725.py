import sys
import numpy as np
input = sys.stdin.readline
v1, v2, v3 = list(map(int, input().split()))
v4 = [list(map(int, input().split())) for v5 in range(v1)]
v6 = 2 ** v1
v7 = float('inf')
for v8 in range(1, v6):
    v9 = []
    for v10 in range(v1):
        if v8 & 1 << v10:
            v9.append(v4[v10 - 1])
    v9 = np.array(v9)
    v11 = sum(v9)
    if all([v11[j] >= v3 for v12 in range(1, v2 + 1)]):
        v7 = min(v7, v11[0])
print(-1 if v7 == float('inf') else v7)
