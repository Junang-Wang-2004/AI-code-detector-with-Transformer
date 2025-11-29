class C1(object):

    def lenLongestFibSubseq(self, a1):
        """
        """
        v1 = set(a1)
        v2 = 2
        for v3 in range(len(a1)):
            for v4 in range(v3 + 1, len(a1)):
                v5, v6, v7 = (a1[v3], a1[v4], 2)
                while v5 + v6 in v1:
                    v5, v6, v7 = (v6, v5 + v6, v7 + 1)
                v2 = max(v2, v7)
        return v2 if v2 > 2 else 0
