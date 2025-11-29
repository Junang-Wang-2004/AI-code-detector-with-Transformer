import sys
import math
input = sys.stdin.readline
v1 = 1000000007
v2 = 1e-06
v3 = int(input())
v4 = []
v5 = []
for v6 in range(v3):
    v7, v8 = map(int, input().split())
    v4.append((v7, v8))
    if v7 == 0:
        v5.append((90.0, v6))
    else:
        v5.append((math.degrees(math.atan(v8 / v7)), v6))
v5.sort()
v9 = 1
v10 = [False] * v3
v11 = v3
for v6 in range(v3):
    v12, v13 = v5[v6]
    if v10[v13]:
        continue
    v10[v13] = True
    if v12 > v2:
        break
    v14 = 1
    v15 = v6 + 1
    while v15 < v3:
        if abs(v12 - v5[v15][0]) <= v2:
            v16 = v5[v15][1]
            if v4[v16][0] * v4[v13][1] == v4[v16][1] * v4[v13][0]:
                v14 += 1
                v10[v16] = True
            v15 += 1
        else:
            break
    v17 = 0
    v18 = v3 - 1
    v19 = v6 + 1
    while v18 - v19 > 1:
        v20 = (v18 + v19) // 2
        if v5[v20][0] >= v12 + 90 - v2:
            v18 = v20
        else:
            v19 = v20
    v15 = v18
    while v15 < v3:
        if abs(v12 + 90 - v5[v15][0]) <= 2e-06:
            v16 = v5[v15][1]
            if v4[v16][0] * v4[v13][0] + v4[v16][1] * v4[v13][1] == 0:
                v17 += 1
                v10[v16] = True
            v15 += 1
        else:
            break
    if v17 != 0:
        v9 = v9 * (pow(2, v14, v1) + pow(2, v17, v1) - 1) % v1
        v11 -= v14 + v17
v9 = v9 * pow(2, v11, v1) % v1 - 1
print(v9)
