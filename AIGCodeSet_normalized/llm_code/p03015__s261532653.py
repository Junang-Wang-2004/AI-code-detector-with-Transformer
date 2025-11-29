v1 = list(map(int, list(input())))
v2 = len(v1) + 1
v3 = 10 ** 9 + 7
v4 = [0 for v5 in range(v2)]
v6 = [0 for v5 in range(v2)]
v4[0] = 1
for v7 in range(1, v2):
    if v1[v7 - 1] == 1:
        v4[v7] = v4[v7 - 1] * 2
        v6[v7] = v4[v7 - 1] + v6[v7 - 1] * 3
        v4[v7] %= v3
        v6[v7] %= v3
    else:
        v4[v7] = v4[v7 - 1] * 2
        v6[v7] = v6[v7 - 1] * 3
        v4[v7] %= v3
        v6[v7] %= v3
print((v4[-1] + v6[-1]) % v3)
