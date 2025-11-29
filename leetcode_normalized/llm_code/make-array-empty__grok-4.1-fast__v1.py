class C1:

    def countOperationsToEmptyArray(self, a1):
        v1 = len(a1)
        v2 = sorted(range(v1), key=a1.__getitem__)
        v3 = v1
        for v4 in range(v1 - 1):
            if v2[v4] > v2[v4 + 1]:
                v3 += v1 - v4 - 1
        return v3
