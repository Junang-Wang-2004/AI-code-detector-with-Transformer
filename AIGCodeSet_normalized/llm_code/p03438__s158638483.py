import sys
import numpy as np
v1 = (int(i) for v2 in input().split())
v3 = [int(v2) for v2 in input().split()]
v4 = [int(v2) for v2 in input().split()]
v5 = sum(v4) - sum(v3)
if sum(v4) == sum(v3):
    v6 = 0
    for v2 in range(0, len(v3)):
        if v3[v2] != v4[v2]:
            v6 = 1
    if v6 == 0:
        print('Yes')
        sys.exit()
if sum(v4) < sum(v3):
    print('No')
    sys.exit()
else:
    v7 = 0
    v8 = 0
    for v2 in range(0, len(v3)):
        if v4[v2] > v3[v2]:
            v7 += v4[v2] - v3[v2]
        if v3[v2] > v4[v2]:
            v8 += v3[v2] - v4[v2]
    if v7 / 2.0 > v5 or v8 / 2.0 > v5:
        print('No')
        sys.exit()
    print('Yes')
