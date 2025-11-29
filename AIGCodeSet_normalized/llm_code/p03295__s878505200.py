(v1, v2), *v3 = [list(map(int, s.split())) for v4 in open(0)]
v3 = [(a - 1, b - 1) for v5, v6 in v3]
v7 = [0] * v1
v8 = [0] * v1
for v5, v6 in v3:
    v7[v5] = 1
    v8[v6] = 1
v9 = False
v10 = 0
for v11, v12 in zip(v7, v8):
    if v12:
        v9 = True
    if v11 and (not v9):
        v10 += 1
    if v11 and v9:
        v9 = False
print(v10)
