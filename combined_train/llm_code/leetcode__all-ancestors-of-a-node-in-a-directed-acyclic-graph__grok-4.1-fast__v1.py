class C1:

    def getAncestors(self, a1, a2):
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v4].append(v3)
        v5 = [None] * a1

        def compute(a1):
            if v5[a1] is not None:
                return v5[a1]
            v1 = set()
            for v2 in v1[a1]:
                v1.add(v2)
                v1 |= compute(v2)
            v5[a1] = v1
            return v1
        v6 = []
        for v7 in range(a1):
            v8 = compute(v7)
            v6.append(sorted(v8))
        return v6
