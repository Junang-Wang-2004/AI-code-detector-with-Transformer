import sys
input = sys.stdin.readline
from itertools import accumulate
v1, v2 = map(int, input().split())
v3 = map(int, input().split())
v4 = accumulate(v3)
v5 = [0] + [(b - i) % v2 for v6, v7 in enumerate(v4, start=1)]
v8 = dict()
v8[v5[0]] = 1
v9 = 0
for v6 in range(1, v1 + 1):
    if v6 >= v2:
        v8[v5[v6 - v2]] = v8.get(v5[v6 - v2], 0) - 1
    v9 += v8.get(v5[v6], 0)
    v8[v5[v6]] = v8.get(v5[v6], 0) + 1
print(v9)
