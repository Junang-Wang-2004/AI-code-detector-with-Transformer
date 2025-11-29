class C1(object):

    def waysToSplitArray(self, a1):
        """
        """
        v1 = sum(a1)
        v2 = v3 = 0
        for v4 in range(len(a1) - 1):
            v3 += a1[v4]
            v2 += int(v3 >= v1 - v3)
        return v2
