class C1(object):

    def maxProductDifference(self, a1):
        """
        """
        v1, v2 = ([0] * 2, [float('inf')] * 2)
        for v3 in a1:
            if v3 >= v1[0]:
                v1[:] = [v3, v1[0]]
            elif v3 > v1[1]:
                v1[1] = v3
            if v3 <= v2[0]:
                v2[:] = [v3, v2[0]]
            elif v3 < v2[1]:
                v2[1] = v3
        return v1[0] * v1[1] - v2[0] * v2[1]
