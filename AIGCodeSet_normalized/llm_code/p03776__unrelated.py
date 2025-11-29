import sys
from itertools import accumulate
v1 = sys.stdin.readline
v2, v3, v4 = map(int, v1().split())
v5 = sorted(map(int, sys.stdin.readlines()), reverse=True)
v6 = [0] + list(accumulate(v5))
v7 = v8 = 0
for v9 in range(v3, v4 + 1):
    v10 = v6[v9] / v9
    if v7 < v10:
        v7 = v10
        v8 = 1
    elif v7 == v10:
        v8 += 1
print(v7)
print(v8)
