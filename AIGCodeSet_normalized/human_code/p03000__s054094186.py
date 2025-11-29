import sys
from operator import itemgetter
v1 = sys.stdin
v2 = lambda: int(ns())
v3 = lambda: list(map(int, v1.readline().split()))
v4 = lambda: v1.readline().rstrip()
v5, v6 = v3()
v7 = v3()
v8 = 1
v9 = 0
for v10 in v7:
    v9 += v10
    if v9 <= v6:
        v8 += 1
print(v8)
