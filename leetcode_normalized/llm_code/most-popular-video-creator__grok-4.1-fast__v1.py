class C1:

    def mostPopularCreator(self, a1, a2, a3):
        v1 = {}
        v2 = {}
        for v3, v4, v5 in zip(a1, a2, a3):
            v1[v3] = v1.get(v3, 0) + v5
            if v3 not in v2 or v5 > v2[v3][0]:
                v2[v3] = (v5, v4)
            elif v5 == v2[v3][0]:
                v2[v3] = (v5, min(v4, v2[v3][1]))
        v6 = max(v1.values())
        v7 = []
        for v3 in v1:
            if v1[v3] == v6:
                v7.append([v3, v2[v3][1]])
        return v7
