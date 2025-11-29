import sys
import numpy as np
from collections import defaultdict
v1 = lambda: sys.stdin.readline().rstrip()
v2 = lambda: int(v1())
v3 = lambda: list(map(int, v1().split()))
v4, v5 = v3()
v6 = np.array([0] + v3())
v6 = (v6 - 1) % v5
v7 = v6.cumsum()
v8 = defaultdict(int)
v9 = 0
for v10, v11 in enumerate(v7):
    v9 += v8[v11]
    v8[v11] += 1
    if v10 >= v5 - 1:
        v8[v7[v10 - (v5 - 1)]] -= 1
print(v9)
