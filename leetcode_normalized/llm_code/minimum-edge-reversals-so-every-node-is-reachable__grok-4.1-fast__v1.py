class C1:

    def minEdgeReversals(self, a1, a2):
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3].append((v4, 0))
            v1[v4].append((v3, 1))

        def get_total(a1, a2):
            v1 = 0
            for v2, v3 in v1[a1]:
                if v2 != a2:
                    v1 += v3 + get_total(v2, a1)
            return v1
        v5 = [0] * a1
        v6 = get_total(0, -1)
        v5[0] = v6

        def reroot(a1, a2, a3):
            for v1, v2 in v1[a1]:
                if v1 != a2:
                    v5[v1] = a3 - v2 + 1 - v2
                    reroot(v1, a1, v5[v1])
        reroot(0, -1, v6)
        return v5
