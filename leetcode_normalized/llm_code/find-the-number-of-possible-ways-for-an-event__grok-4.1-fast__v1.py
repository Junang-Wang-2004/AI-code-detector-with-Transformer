v1 = 10 ** 9 + 7
v2 = 1005
v3 = [[0] * v2 for v4 in range(v2)]
v5 = [[0] * v2 for v4 in range(v2)]
v6 = [[1] * v2 for v4 in range(v2)]
v3[0][0] = 1
for v7 in range(1, v2):
    v3[v7][0] = 1
    for v8 in range(1, v7 + 1):
        if v8 < v2:
            v3[v7][v8] = (v3[v7 - 1][v8] + v3[v7 - 1][v8 - 1]) % v1
v5[0][0] = 1
for v7 in range(1, v2):
    for v8 in range(1, v7 + 1):
        if v8 < v2:
            v9 = v8 * v5[v7 - 1][v8] % v1
            v10 = v8 * v5[v7 - 1][v8 - 1] % v1
            v5[v7][v8] = (v9 + v10) % v1
for v11 in range(1, v2):
    for v12 in range(1, v2):
        v6[v11][v12] = v6[v11][v12 - 1] * v11 % v1

class C1(object):

    def numberOfWays(self, a1, a2, a3):
        v1 = 0
        v2 = min(a1, a2)
        for v3 in range(1, v2 + 1):
            v4 = v3[a2][v3] * v5[a1][v3] % v1
            v4 = v4 * v6[a3][v3] % v1
            v1 = (v1 + v4) % v1
        return v1
