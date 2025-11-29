import math
v1, v2, v3, v4 = map(int, input().split())
v5 = math.sqrt((v1 - v3) ** 2 + (v2 - v4) ** 2)
v6 = []
v7 = []
v8 = 0
for v9 in range(-200, 201):
    if v8 == 1:
        break
    for v10 in range(-200, 201):
        v11 = math.sqrt((v9 - v3) ** 2 + (v10 - v4) ** 2)
        v12 = math.sqrt((v9 - v1) ** 2 + (v10 - v2) ** 2)
        if v11 == v5 and v12 == math.sqrt(2) * v5:
            v6.append(v9)
            v6.append(v10)
            v8 = 1
            break
v9, v10 = map(int, [k for v13 in v6])
v14, v15 = ((v1 + v9) / 2, (v2 + v10) / 2)
v16 = 2 * v14 - v3
v17 = 2 * v15 - v4
print(v9, v10, v16, v17)
