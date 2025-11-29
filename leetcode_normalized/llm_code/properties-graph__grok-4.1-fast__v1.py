class C1:

    def numberOfComponents(self, a1, a2):
        v1 = len(a1)
        v2 = [set(p) for v3 in a1]
        v4 = list(range(v1))

        def find(a1):
            if v4[a1] != a1:
                v4[a1] = find(v4[a1])
            return v4[a1]

        def unite(a1, a2):
            v1 = find(a1)
            v2 = find(a2)
            if v1 != v2:
                v4[v1] = v2
        for v5 in range(v1):
            for v6 in range(v5 + 1, v1):
                if len(v2[v5] & v2[v6]) >= a2:
                    unite(v5, v6)
        v7 = set((find(v5) for v5 in range(v1)))
        return len(v7)
