class C1:

    def kBigIndices(self, a1, a2):
        v1 = len(a1)
        v2 = sorted(set(a1))
        v3 = {v: i + 1 for v4, v5 in enumerate(v2)}
        v6 = len(v2)

        def update(a1, a2, a3):
            while a2 <= v6:
                a1[a2] += a3
                a2 += a2 & -a2

        def query(a1, a2):
            v1 = 0
            while a2 > 0:
                v1 += a1[a2]
                a2 -= a2 & -a2
            return v1
        v7 = [False] * v1
        v8 = [0] * (v6 + 2)
        for v4 in range(v1):
            v9 = v3[a1[v4]]
            v7[v4] = query(v8, v9 - 1) >= a2
            update(v8, v9, 1)
        v10 = [False] * v1
        v8 = [0] * (v6 + 2)
        for v4 in range(v1 - 1, -1, -1):
            v9 = v3[a1[v4]]
            v10[v4] = query(v8, v9 - 1) >= a2
            update(v8, v9, 1)
        return sum((v7[v4] and v10[v4] for v4 in range(v1)))
