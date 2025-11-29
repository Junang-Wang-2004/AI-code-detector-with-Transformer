import sys
from bisect import bisect_left
v1 = sys.stdin.readline
v2, v3 = map(int, v1().split())
v4 = sorted(map(int, v1().split()))
v5 = 0
for v6 in range(v2):
    v7 = v4[v3 - v6 - 1]
    v8 = bisect_left(v4, v7)
    v9 = v4[v6] * (v6 + 1) + v7 * (v2 - v8)
    v5 = max(v5, v9)
print(v5)
