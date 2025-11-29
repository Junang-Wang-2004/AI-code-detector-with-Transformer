v1 = int(input())
v2 = []
for v3 in range(v1):
    v4 = int(input())
    v2.append(v4)
v5 = [0 for v3 in range(v1 + 1)]
v5[0] = 1
v6 = 10 ** 9 + 7
v7 = [0 for v3 in range(2 * 10 ** 5 + 1)]
for v3 in range(v1):
    v4 = v2[v3]
    if v7[v4] == 0:
        v5[v3 + 1] = v5[v3]
        v7[v4] = v3 + 1
        continue
    elif v7[v4] != 0:
        if v7[v4] == v3:
            v7[v4] = v3 + 1
            v5[v3 + 1] = v5[v3]
        else:
            v5[v3 + 1] = (v5[v3] + v5[v7[v4]]) % v6
            v7[v4] = v3 + 1
print(v5[v1] % v6)
