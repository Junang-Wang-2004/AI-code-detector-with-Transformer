class C1:

    def numberOfPoints(self, a1):
        if not a1:
            return 0
        v1 = sorted(a1)
        v2 = []
        for v3, v4 in v1:
            if not v2 or v2[-1][1] < v3:
                v2.append([v3, v4])
            else:
                v2[-1][1] = max(v2[-1][1], v4)
        v5 = 0
        for v3, v4 in v2:
            v5 += v4 - v3 + 1
        return v5
