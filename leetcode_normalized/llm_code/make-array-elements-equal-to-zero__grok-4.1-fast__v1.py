class C1:

    def countValidSelections(self, a1):
        v1 = sum(a1)
        v2 = 0
        v3 = 0
        for v4 in a1:
            if v4 == 0:
                v5 = abs(2 * v3 - v1)
                v2 += max(2 - v5, 0)
            v3 += v4
        return v2
