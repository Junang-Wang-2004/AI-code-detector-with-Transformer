import sys
from itertools import product
v1, v2, v3 = map(int, sys.stdin.readline().split())
v4 = [list(map(int, sys.stdin.readline().split())) for v5 in range(v1)]
v6 = float('inf')
for v7 in product(range(2), repeat=v1):
    v8 = [0] * v2
    v9 = 0
    for v10 in range(v1):
        if v7[v10]:
            v9 += v4[v10][0]
            for v11 in range(v2):
                v8[v11] += v4[v10][v11 + 1]
    if all((level >= v3 for v12 in v8)):
        v6 = min(v6, v9)
print(v6 if v6 != float('inf') else -1)
