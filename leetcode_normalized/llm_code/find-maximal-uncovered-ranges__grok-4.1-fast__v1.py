class C1:

    def findMaximalUncoveredRanges(self, a1, a2):
        v1 = sorted(a2)
        v2 = []
        for v3, v4 in v1:
            if not v2 or v2[-1][1] < v3:
                v2.append([v3, v4])
            else:
                v2[-1][1] = max(v2[-1][1], v4)
        v5 = []
        v6 = -1
        for v7, v8 in v2:
            if v6 + 1 < v7:
                v5.append([v6 + 1, v7 - 1])
            v6 = max(v6, v8)
        if v6 + 1 < a1:
            v5.append([v6 + 1, a1 - 1])
        return v5
