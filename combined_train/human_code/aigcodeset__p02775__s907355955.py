v1 = input()
v2 = len(v1)
v3 = 0
v4 = [0] * (v2 + 1)
v5 = [0] * (v2 + 1)
v4[0] = 1
for v6 in range(v2):
    v7 = int(v1[v6])
    if v7 < 5:
        v5[v6 + 1] = v5[v6] + v7
    elif v7 > 5:
        v5[v6 + 1] = v4[v6] + 10 - v7
    elif v6 == 0:
        v5[v6 + 1] = v5[v6] + v7
    elif int(v1[v6 - 1]) < 5:
        v5[v6 + 1] = v5[v6] + v7
    else:
        v5[v6 + 1] = v4[v6] + 10 - v7
    v7 += 1
    if v7 == 10:
        v4[v6 + 1] = v4[v6]
    elif v7 < 5:
        v4[v6 + 1] = v5[v6] + v7
    elif v7 > 5:
        v4[v6 + 1] = v4[v6] + 10 - v7
    elif v6 == 0:
        v4[v6 + 1] = v5[v6] + v7
    elif int(v1[v6 - 1]) < 5:
        v4[v6 + 1] = v5[v6] + v7
    else:
        v4[v6 + 1] = v4[v6] + 10 - v7
print(v5[v2])
