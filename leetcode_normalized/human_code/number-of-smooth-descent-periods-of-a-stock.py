class C1(object):

    def getDescentPeriods(self, a1):
        """
        """
        v1 = v2 = 0
        for v3 in range(len(a1)):
            v2 += 1
            if v3 + 1 == len(a1) or a1[v3] - 1 != a1[v3 + 1]:
                v1 += v2 * (v2 + 1) // 2
                v2 = 0
        return v1
