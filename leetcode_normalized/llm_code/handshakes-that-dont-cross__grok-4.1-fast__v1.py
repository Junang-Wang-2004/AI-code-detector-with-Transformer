class C1:

    def numberOfWays(self, a1):
        v1 = 10 ** 9 + 7
        v2 = a1 // 2
        v3 = 1
        for v4 in range(1, v2 + 1):
            v3 = v3 * (4 * v4 - 2) % v1 * pow(v4 + 1, v1 - 2, v1) % v1
        return v3
