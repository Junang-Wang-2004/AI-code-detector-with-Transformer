class C1(object):

    def getAverages(self, a1, a2):
        """
        """
        v1, v2 = (0, 2 * a2 + 1)
        v3 = [-1] * len(a1)
        for v4 in range(len(a1)):
            v1 += a1[v4]
            if v4 - v2 >= 0:
                v1 -= a1[v4 - v2]
            if v4 >= v2 - 1:
                v3[v4 - a2] = v1 // v2
        return v3
