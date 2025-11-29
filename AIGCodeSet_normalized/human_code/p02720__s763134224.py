v1 = int(input())
v2 = list(range(1, 10))
v3 = v2[:]
v4 = 0
while len(v3) < v1:
    v5 = []
    for v6 in v2:
        v7, v8 = divmod(v6, 10)
        if v8 != 0:
            v5.append(v6 * 10 + v8 - 1)
        v5.append(v6 * 10 + v8)
        if v8 != 9:
            v5.append(v6 * 10 + v8 + 1)
    v2 = v5
    v3 += v5
print(v3[v1 - 1])
