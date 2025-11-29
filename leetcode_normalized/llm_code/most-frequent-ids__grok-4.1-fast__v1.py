class C1:

    def mostFrequentIDs(self, a1, a2):
        v1 = {}
        v2 = 0
        v3 = []
        for v4, v5 in zip(a1, a2):
            v6 = v1.get(v4, 0)
            v1[v4] = v6 + v5
            if v1[v4] > v2:
                v2 = v1[v4]
            v3.append(v2)
        return v3
