import sys
import math
import numpy as np
import itertools
v1, v2 = (int(i) for v3 in input().split())
if (v1 - 2) * (v1 - 1) // 2 < v2:
    print('-1')
    exit()
v4 = v1 * (v1 - 1) // 2 - v2
print(v4)
v5 = 0
v6 = 1
for v3 in range(v4):
    print(v5 + 1, v6 + 1)
    v6 += 1
    if v6 == v1:
        v5 += 1
        v6 = v5 + 1
