import sys
v1 = sys.stdin.readline
v2, v3, v4 = map(int, v1().split())
v5 = 10 ** 10
v6 = [[v5] * 401 for v7 in range(401)]
v6[0][0] = 0
for v8 in range(v2):
    v9, v10, v11 = map(int, v1().split())
    for v7 in range(len(v6) - 1, -1, -1):
        for v12 in range(len(v6[v7]) - 1, -1, -1):
            if v6[v7][v12] == v5:
                continue
            v6[v7 + v9][v12 + v10] = min(v6[v7 + v9][v12 + v10], v6[v7][v12] + v11)
v13 = v5
import math
for v7 in range(1, len(v6)):
    for v12 in range(1, len(v6)):
        v14 = math.gcd(v7, v12)
        if v7 // v14 == v3 and v12 // v14 == v4:
            if v13 > v6[v7][v12]:
                v13 = v6[v7][v12]
if v13 == v5:
    print(-1)
else:
    print(v13)
