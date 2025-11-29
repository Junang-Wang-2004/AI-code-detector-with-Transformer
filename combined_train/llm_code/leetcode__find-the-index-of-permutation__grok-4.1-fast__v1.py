class C1:

    def getPermutationIndex(self, a1):
        v1 = 1000000007
        v2 = len(a1)
        v3 = [1] * (v2 + 1)
        for v4 in range(1, v2 + 1):
            v3[v4] = v3[v4 - 1] * v4 % v1
        v5 = [0] * (v2 + 2)

        def update(a1, a2):
            while a1 <= v2:
                v5[a1] = (v5[a1] + a2) % v1
                a1 += a1 & -a1

        def prefix_sum(a1):
            v1 = 0
            while a1 > 0:
                v1 = (v1 + v5[a1]) % v1
                a1 -= a1 & -a1
            return v1
        v6 = 0
        for v7 in range(v2):
            v8 = a1[v7]
            v9 = prefix_sum(v8 - 1)
            v10 = (v8 - 1 - v9) % v1
            v6 = (v6 + v10 * v3[v2 - 1 - v7] % v1) % v1
            update(v8, 1)
        return v6
