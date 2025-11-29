class C1:

    def largestSquareArea(self, a1, a2):

        def overlap_side(a1, a2, a3, a4):
            v1 = max(a1[0], a3[0])
            v2 = min(a2[0], a4[0])
            v3 = max(a1[1], a3[1])
            v4 = min(a2[1], a4[1])
            v5 = max(0, v2 - v1)
            v6 = max(0, v4 - v3)
            return min(v5, v6)
        v1 = len(a1)
        v2 = 0
        for v3 in range(v1):
            for v4 in range(v3 + 1, v1):
                v5 = overlap_side(a1[v3], a2[v3], a1[v4], a2[v4])
                if v5 > v2:
                    v2 = v5
        return v2 * v2
