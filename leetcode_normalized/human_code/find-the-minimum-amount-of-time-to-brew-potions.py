class C1(object):

    def minTime(self, a1, a2):
        """
        """
        v1 = 0
        for v2 in range(1, len(a2)):
            v3 = v4 = 0
            for v5 in a1:
                v3 += v5
                v4 = max(v4, a2[v2 - 1] * v3 - a2[v2] * (v3 - v5))
            v1 += v4
        v1 += a2[-1] * sum(a1)
        return v1
