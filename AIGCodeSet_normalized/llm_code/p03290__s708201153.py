import math
v1, v2 = map(int, input().split())
v3 = []
for v4 in range(0, v1):
    v3.append(list(map(int, input().split())))
v5 = [0] * v1
for v4 in range(0, v1):
    v5[v4] = (v4 + 1) * 100 * v3[v4][0] + v3[v4][1]
v6 = [0] * v1
for v4 in range(0, v1):
    v6[v4] = v5[v4] / v3[v4][0]
v7 = 0
v8 = max(v6)
v9 = v6.index(v8)
while v2 >= v5[v9]:
    v2 -= v5[v9]
    v7 += v3[v9][0]
    v6[v9] = 0
    v5[v9] = 0
    v3[v9] = [0, 0]
    v8 = max(v6)
    v9 = v6.index(v8)
v10 = [0] * v1
for v4 in range(0, v1):
    if v2 > v5[v4]:
        v10[v4] = math.inf
    elif v2 > v3[v4][0] * (v4 + 1) * 100:
        v10[v4] = v3[v4][0]
    else:
        v10[v4] = math.ceil(v2 / (100 * (v4 + 1)))
v11 = min(v10)
print(int(v7 + v11))
