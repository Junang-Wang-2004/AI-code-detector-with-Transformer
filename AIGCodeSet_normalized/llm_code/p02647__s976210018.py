import sys
import math
input = lambda: sys.stdin.readline().rstrip()
v1, v2 = map(int, input().split())
v3 = list(map(int, ('0 ' + input()).split()))
v4 = math.log(v1) + 1
for v5 in range(min(v2, v4)):
    v6 = [0 for v7 in range(v1 + 1)]
    for v8 in range(1, v1 + 1):
        v9 = max(1, v8 - v3[v8])
        v10 = min(v1, v8 + v3[v8])
        v6[v9] += 1
        if v10 + 1 <= v1:
            v6[v10 + 1] -= 1
    v11 = 0
    for v8 in range(len(v6)):
        v11 += v6[v8]
        v3[v8] = v11
for v8 in v3[1:]:
    print(v8)
