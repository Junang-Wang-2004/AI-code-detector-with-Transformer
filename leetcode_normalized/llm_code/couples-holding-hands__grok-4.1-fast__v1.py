class C1:

    def minSwapsCouples(self, a1):
        v1 = len(a1) // 2
        v2 = [0] * (2 * v1)
        for v3, v4 in enumerate(a1):
            v2[v4] = v3 // 2
        v5 = list(range(v1))
        v6 = [0] * v1

        def find(a1):
            if v5[a1] != a1:
                v5[a1] = find(v5[a1])
            return v5[a1]

        def unite(a1, a2):
            v1 = find(a1)
            v2 = find(a2)
            if v1 != v2:
                if v6[v1] < v6[v2]:
                    v5[v1] = v2
                elif v6[v1] > v6[v2]:
                    v5[v2] = v1
                else:
                    v5[v2] = v1
                    v6[v1] += 1
        for v7 in range(v1):
            unite(v2[2 * v7], v2[2 * v7 + 1])
        v8 = set((find(v3) for v3 in range(v1)))
        return v1 - len(v8)
