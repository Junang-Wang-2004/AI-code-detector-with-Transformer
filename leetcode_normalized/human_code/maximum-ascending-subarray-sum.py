class C1(object):

    def maxAscendingSum(self, a1):
        """
        """
        v1 = v2 = 0
        for v3 in range(len(a1)):
            if not (v3 and a1[v3 - 1] < a1[v3]):
                v2 = 0
            v2 += a1[v3]
            v1 = max(v1, v2)
        return v1
