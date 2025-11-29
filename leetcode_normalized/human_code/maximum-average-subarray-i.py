class C1(object):

    def findMaxAverage(self, a1, a2):
        """
        """
        v1 = v2 = sum(a1[:a2])
        for v3 in range(a2, len(a1)):
            v2 += a1[v3] - a1[v3 - a2]
            v1 = max(v1, v2)
        return float(v1) / a2
