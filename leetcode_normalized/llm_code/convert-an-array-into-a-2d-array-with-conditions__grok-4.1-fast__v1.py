class C1:

    def findMatrix(self, a1):
        v1 = {}
        for v2 in a1:
            v1[v2] = v1.get(v2, 0) + 1
        if not v1:
            return []
        v3 = max(v1.values())
        v4 = [[] for v5 in range(v3)]
        for v6, v7 in v1.items():
            for v8 in range(v7):
                v4[v8].append(v6)
        return v4
