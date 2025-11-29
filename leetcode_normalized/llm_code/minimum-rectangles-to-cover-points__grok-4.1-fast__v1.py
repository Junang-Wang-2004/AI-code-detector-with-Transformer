class C1:

    def minRectanglesToCoverPoints(self, a1, a2):
        v1 = sorted((p[0] for v2 in a1))
        v3 = len(v1)
        v4 = 0
        v5 = 0
        while v5 < v3:
            v4 += 1
            v6 = v1[v5]
            while v5 < v3 and v1[v5] <= v6 + a2:
                v5 += 1
        return v4
