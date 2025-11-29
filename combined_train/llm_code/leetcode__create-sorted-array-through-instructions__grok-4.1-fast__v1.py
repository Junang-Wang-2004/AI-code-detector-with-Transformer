class C1:

    def createSortedArray(self, a1):
        v1 = 10 ** 9 + 7
        if not a1:
            return 0
        v2 = sorted(set(a1))
        v3 = {v2[i]: i + 1 for v4 in range(len(v2))}
        v5 = len(v2)
        v6 = [0] * (v5 + 1)

        def update_ft(a1, a2):
            while a1 <= v5:
                v6[a1] += a2
                a1 += a1 & -a1

        def prefix_sum(a1):
            v1 = 0
            while a1 > 0:
                v1 += v6[a1]
                a1 -= a1 & -a1
            return v1
        v7 = 0
        v8 = 0
        for v9 in a1:
            v10 = v3[v9]
            v11 = prefix_sum(v10 - 1)
            v12 = prefix_sum(v10)
            v13 = v8 - v12
            v7 = (v7 + min(v11, v13)) % v1
            update_ft(v10, 1)
            v8 += 1
        return v7
