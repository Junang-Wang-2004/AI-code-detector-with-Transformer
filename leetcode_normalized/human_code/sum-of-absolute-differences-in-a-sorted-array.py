class C1(object):

    def getSumAbsoluteDifferences(self, a1):
        """
        """
        v1, v2 = (0, sum(a1))
        v3 = []
        for v4, v5 in enumerate(a1):
            v2 -= v5
            v3.append(v4 * v5 - v1 + (v2 - (len(a1) - 1 - v4) * v5))
            v1 += v5
        return v3
