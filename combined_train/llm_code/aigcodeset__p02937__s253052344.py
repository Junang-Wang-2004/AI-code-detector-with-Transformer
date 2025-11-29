import sys
from bisect import bisect_left, bisect_right
v1 = sys.stdin.readline().strip()
v2 = sys.stdin.readline().strip()
v3 = len(v1)
v4 = {}
for v5, v6 in enumerate(v1 * 2):
    if v6 not in v4:
        v4[v6] = [v5]
    else:
        v4[v6].append(v5)
v7 = 0
v8 = 0
for v9 in v2:
    if v9 not in v4:
        print(-1)
        quit()
    v10 = bisect_left(v4[v9], v7)
    v7 = v4[v9][v10]
    if v3 <= v7:
        v8 += 1
        v7 -= v3
print(v8 * v3 + v7 + 1)
