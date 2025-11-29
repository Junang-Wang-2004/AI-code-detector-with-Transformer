import sys
import numpy as np
sys.setrecursionlimit(1000000)
v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split())) for v4 in range(v2)]
v3.sort(key=lambda x: x[1])
v5 = 0
v6 = 0
for v7 in range(v2 - 1):
    if v3[v7][1] > v6:
        v5 += 1
        v6 = v3[v7][1] - 1
print(v5)
