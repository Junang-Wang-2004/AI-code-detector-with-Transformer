class C1:

    def countSmaller(self, a1):
        if not a1:
            return []
        v1 = sorted(set(a1))
        v2 = {v: i + 1 for v3, v4 in enumerate(v1)}
        v5 = len(v1)
        v6 = [0] * (v5 + 1)
        v7 = [0] * len(a1)

        def modify(a1, a2):
            while a1 <= v5:
                v6[a1] += a2
                a1 += a1 & -a1

        def prefix_sum(a1):
            v1 = 0
            while a1 > 0:
                v1 += v6[a1]
                a1 -= a1 & -a1
            return v1
        for v8 in range(len(a1) - 1, -1, -1):
            v9 = v2[a1[v8]]
            v7[v8] = prefix_sum(v9 - 1)
            modify(v9, 1)
        return v7
