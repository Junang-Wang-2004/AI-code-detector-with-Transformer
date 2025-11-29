class C1:

    def minUnlockedIndices(self, a1, a2):
        v1 = 0
        v2 = 0
        v3 = 0
        for v4, v5 in zip(a1, a2):
            if v4 > v2:
                v2 = v4
                v3 = 0
            elif v4 < v2:
                if v2 != v4 + 1:
                    return -1
                v1 += v3
                v3 = 0
            v3 += v5
        return v1
