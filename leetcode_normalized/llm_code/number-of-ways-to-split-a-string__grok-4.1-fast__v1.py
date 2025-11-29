class C1:

    def numWays(self, a1):
        v1 = 10 ** 9 + 7
        v2 = len(a1)
        v3 = sum((c == '1' for v4 in a1))
        if v3 % 3:
            return 0
        v5 = v3 // 3
        if v5 == 0:
            return (v2 - 1) * (v2 - 2) // 2 % v1
        v6 = [0] * (v2 + 1)
        for v7 in range(v2):
            v6[v7 + 1] = v6[v7] + (a1[v7] == '1')
        v8 = v6.count(v5)
        v9 = v6.count(2 * v5)
        return v8 * v9 % v1
