v1, v2, v3 = map(int, input().split())
v4 = v2 % v3
v5 = v4
v6 = [v4]
for v7 in range(v1 - 1):
    v4 = v4 ** 2 % v3
    if v4 == 0:
        break
    elif v4 == v6[0]:
        v8 = len(v6)
        v9 = v1 // v8
        v10 = v1 % v8
        v5 = v5 + v5 * v9
        for v11 in range(v10):
            v5 += v6[v10]
        break
    else:
        v5 += v4
        v6.append(v4)
print(v5)
