class C1:

    def sortByAbsoluteValue(self, a1):
        v1 = 0
        for v2 in a1:
            v1 = max(v1, abs(v2))
        v3 = [[] for v4 in range(v1 + 1)]
        for v2 in a1:
            v3[abs(v2)].append(v2)
        v5 = []
        for v6 in v3:
            v5.extend(v6)
        return v5
