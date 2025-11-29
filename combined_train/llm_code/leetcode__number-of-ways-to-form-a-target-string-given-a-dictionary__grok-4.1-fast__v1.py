class C1:

    def numWays(self, a1, a2):
        v1 = 10 ** 9 + 7
        if not a1 or not a2:
            return int(not a2)
        v2 = len(a1[0])
        v3 = len(a2)
        v4 = ord('a')
        v5 = [[0] * 26 for v6 in range(v2)]
        for v7 in range(v2):
            for v8 in a1:
                v9 = ord(v8[v7]) - v4
                v5[v7][v9] += 1
        v10 = [[0] * (v3 + 1) for v6 in range(v2 + 1)]
        for v7 in range(v2 + 1):
            v10[v7][0] = 1
        for v7 in range(1, v2 + 1):
            for v11 in range(1, v3 + 1):
                v12 = ord(a2[v11 - 1]) - v4
                v10[v7][v11] = (v10[v7 - 1][v11] + v10[v7 - 1][v11 - 1] * v5[v7 - 1][v12]) % v1
        return v10[v2][v3]
