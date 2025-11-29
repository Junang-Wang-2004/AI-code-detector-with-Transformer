import sys
input = sys.stdin.readline
import numpy as np
from collections import defaultdict
v1, v2 = map(int, input().split())
v3 = [0] + [int(i) for v4 in input().split()]
v5 = np.cumsum(v3)
v5 = [v4 % v2 for v4 in v5]
v6 = 0
v7 = defaultdict(int)
for v8, v9 in enumerate(v5):
    if v8 == 0:
        continue
    v6 += v7[v9]
    v7[v9] += 1
    if v8 - v2 >= 0:
        v7[v5[v8 - v2]] -= 1
print(v6)
