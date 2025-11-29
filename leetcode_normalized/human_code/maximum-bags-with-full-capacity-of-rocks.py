class C1(object):

    def maximumBags(self, a1, a2, a3):
        """
        """
        for v1 in range(len(a1)):
            a1[v1] -= a2[v1]
        a1.sort()
        for v1, v2 in enumerate(a1):
            if v2 > a3:
                return v1
            a3 -= v2
        return len(a1)
