import math
import itertools
from collections import deque
from collections import Counter
from fractions import gcd
import bisect
v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = [0] * v1
v3.sort()
v4[0] = v3[0]
for v5 in range(1, v1):
    v4[v5] = v4[v5 - 1] + v3[v5]
v6 = 0
v7 = 0
v8 = 2 * v3[-1] + 1
while v8 > v7 + 1:
    v9 = (v7 + v8) // 2
    v6 = 0
    for v10 in v3:
        v11 = v9 - v10
        v12 = bisect.bisect_left(v3, v11)
        v6 += v1 - v12
    if v6 < v2:
        v8 = v9
    else:
        v7 = v9
v13 = 0
v14 = 0
for v10 in v3:
    v12 = bisect.bisect_left(v3, v7 - v10)
    v13 = v13 + v10 * (v1 - v12) + (v4[-1] - v4[v12 - 1]) if v12 != 0 else v13 + v10 * (v1 - v12) + v4[-1]
    v14 += v1 - v12
v13 -= (v14 - v2) * v7
print(v13)
