from functools import reduce
v1 = 10 ** 9 + 7
v2 = v3 = v4 = 1000
v5 = min(v2, v3)
v6 = [[0] * (v2 + 1) for v7 in range(v2 + 1)]
v8 = [[0] * (v2 + 1) for v7 in range(v2 + 1)]
v6[0][0] = v8[0][0] = 1
for v9 in range(1, v2 + 1):
    v6[v9][0] = 1
    for v10 in range(1, v9 + 1):
        v6[v9][v10] = (v6[v9 - 1][v10] + v6[v9 - 1][v10 - 1]) % v1
        v8[v9][v10] = (v8[v9 - 1][v10] * v10 + v8[v9 - 1][v10 - 1] * v10) % v1
v11 = [[1] * (v5 + 1) for v7 in range(v4 + 1)]
for v9 in range(1, v4 + 1):
    for v10 in range(1, v5 + 1):
        v11[v9][v10] = v11[v9][v10 - 1] * v9 % v1

class C1(object):

    def numberOfWays(self, a1, a2, a3):
        """
        """
        return reduce(lambda accu, x: (accu + a2) % v1, (v6[a2][v9] * v8[a1][v9] * v11[a3][v9] for v9 in range(1, min(a1, a2) + 1)), 0)
