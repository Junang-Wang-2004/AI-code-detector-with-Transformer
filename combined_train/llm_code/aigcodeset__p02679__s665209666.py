import sys
import math
from collections import Counter
v1 = 1000000007
v2 = int(sys.stdin.readline().strip())
v3 = []
v4 = 0
v5 = 0
v6 = 0
v7 = v2
for v8 in range(v2):
    v9, v10 = map(int, sys.stdin.readline().strip().split())
    if v9 == 0 and v10 == 0:
        v4 += 1
        v7 -= 1
    elif v9 == 0:
        v5 += 1
    elif v10 == 0:
        v6 += 1
    else:
        v11 = math.gcd(v9, v10)
        v3.append((v9 // v11, v10 // v11))
v12 = Counter(v3)
v13 = set()
v14 = 1
for (v9, v10), v15 in v12.items():
    if (v9, v10) in v13:
        continue
    v16 = 0
    for v17, v18 in ((-1, 1), (1, -1)):
        v19 = (v10 * v17, v9 * v18)
        if v19 in v12:
            v16 += v12[v19]
            v13.add(v19)
    if v16 == 0:
        v14 *= 2 ** v15
        v14 %= v1
    else:
        v20 = 2 ** v15
        v21 = 2 ** v16
        v14 *= v20 + v21 - 1
        v14 %= v1
    v7 -= v15 + v16
if (1, 0) not in v12:
    v12[1, 0] = 0
if (0, 1) not in v12:
    v12[0, 1] = 0
if (0, 0) not in v12:
    v12[0, 0] = 0
v14 *= 2 ** v12[1, 0] + 2 ** v12[0, 1] - 1
v14 %= v1
v7 -= v6 + v5
v14 *= pow(2, v7, v1)
v14 = (v14 + v4 - 1) % v1
print(v14)
