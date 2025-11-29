import numpy as np
from scipy.sparse.csgraph import dijkstra
from collections import defaultdict
import sys
input = sys.stdin.readline
[v1, v2] = [int(x) for v3 in input().split()]
v4 = np.array([[int(v3) for v3 in input().split()] for v5 in range(10)])
v6 = []
for v5 in range(v1):
    v6 += [int(v3) for v3 in input().split()]
v7 = defaultdict(int)
for v8 in v6:
    if v8 != 1 and v8 != -1:
        v7[v8] += 1
v9 = 0
for v10, v11 in v7.items():
    v9 += v11 * int(dijkstra(v4, indices=v10)[1])
print(v9)
