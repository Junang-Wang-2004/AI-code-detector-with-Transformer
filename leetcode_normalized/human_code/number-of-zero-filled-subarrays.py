class C1(object):

    def zeroFilledSubarray(self, a1):
        """
        """
        v1 = 0
        v2 = -1
        for v3 in range(len(a1)):
            if a1[v3]:
                v2 = v3
                continue
            v1 += v3 - v2
        return v1
