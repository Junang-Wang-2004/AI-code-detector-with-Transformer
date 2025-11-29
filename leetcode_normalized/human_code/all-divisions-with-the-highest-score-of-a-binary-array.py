class C1(object):

    def maxScoreIndices(self, a1):
        """
        """
        v1 = []
        v2 = v3 = 0
        v4 = sum(a1)
        for v5 in range(len(a1) + 1):
            v3 += (a1[v5 - 1] if v5 else 0) == 0
            if v3 + (v4 - (v5 - v3)) > v2:
                v2 = v3 + (v4 - (v5 - v3))
                v1 = []
            if v3 + (v4 - (v5 - v3)) == v2:
                v1.append(v5)
        return v1
