from collections import defaultdict
import sys
v1 = sys.stdin.readline
v2, v3 = map(int, v1().split())
v4 = []
for v5 in range(v2):
    v4.append(tuple(map(int, v1().split())))
v6 = defaultdict(int)
for v7, v8 in v4:
    v6[v7] += v8
v9 = sorted(v6.keys())
v10 = v3
v11 = 0
while v10 > 0:
    v10 -= v6[v9[v11]]
    v12 = v9[v11]
    v11 += 1
print(v12)
