v1, v2, v3 = map(int, input().split())
v4 = [0] * v3
v5 = 0
v6 = v2
v4[v6 - 1] = 1
v7 = 0
for v8 in range(1, v3):
    v6 = v6 * v6 % v3
    if v4[v6 - 1] == 0:
        v4[v6 - 1] = v8 + 1
    else:
        v9 = v4[v6 - 1]
        v10 = v8 + 1
        v7 = v10 - v9
        break
v6 = v2
for v8 in range(v9):
    v5 += v6
    v6 = v6 * v6 % v3
if v7 != 0:
    v11, v12 = ((v1 - v9) // v7, (v1 - v9) % v7)
    v13 = 0
    for v8 in range(v7):
        v13 += v6
        v6 = v6 * v6 % v3
    v5 += v13 * v11
    for v8 in range(v12):
        v5 += v6
        v6 = v6 * v6 % v3
print(v5)
