class C1:

    def countOfPairs(self, a1):
        v1 = 10 ** 9 + 7
        if not a1:
            return 0
        v2 = max(a1)
        v3 = [0] * (v2 + 1)
        for v4 in range(a1[0] + 1):
            v3[v4] = 1
        for v5 in range(1, len(a1)):
            v6 = max(a1[v5] - a1[v5 - 1], 0)
            v7 = [0] * (v2 + 2)
            for v8 in range(1, v2 + 2):
                v7[v8] = (v7[v8 - 1] + v3[v8 - 1]) % v1
            v9 = [0] * (v2 + 1)
            for v10 in range(a1[v5] + 1):
                v11 = v10 - v6
                if v11 >= 0:
                    v9[v10] = v7[v11 + 1]
            v3 = v9
        return sum(v3) % v1
