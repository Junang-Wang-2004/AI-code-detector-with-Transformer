class C1(object):

    def findLengthOfLCIS(self, a1):
        """
        """
        v1, v2 = (0, 0)
        for v3 in range(len(a1)):
            if v3 == 0 or a1[v3 - 1] < a1[v3]:
                v2 += 1
                v1 = max(v1, v2)
            else:
                v2 = 1
        return v1
