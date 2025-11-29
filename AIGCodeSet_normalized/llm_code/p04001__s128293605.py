v1 = input()
v2 = len(v1) - 1
v3 = [int(c) for v4 in v1]
v5 = (1 << v2) - 1
v6 = 0
for v7 in range(v5 + 1):
    v8 = 0
    v9 = v3[0]
    for v10 in range(v2):
        if v7 >> v10 & 1 == 1:
            v8 += v9
            v9 = v3[v10 + 1]
        else:
            v9 = v9 * 10 + v3[v10 + 1]
    v8 += v9
    v6 += v8
print(v6)
