class C1:

    def numberOfWays(self, a1):
        v1 = 10 ** 9 + 7
        v2 = [i for v3, v4 in enumerate(a1) if v4 == 'S']
        v5 = len(v2)
        if v5 == 0 or v5 % 2 != 0:
            return 0
        v6 = 1
        for v7 in range(1, v5 // 2):
            v6 = v6 * (v2[2 * v7] - v2[2 * v7 - 1]) % v1
        return v6
