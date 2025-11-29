class C1(object):

    def arrayPairSum(self, a1):
        """
        """
        a1.sort()
        v1 = 0
        for v2 in range(0, len(a1), 2):
            v1 += a1[v2]
        return v1
