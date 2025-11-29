class C1(object):

    def maxSubstrings(self, a1):
        """
        """
        v1 = 4
        v2 = 0
        v3 = {}
        for v4, v5 in enumerate(a1):
            if v5 not in v3:
                v3[v5] = v4
            elif v4 - v3[v5] + 1 >= v1:
                v2 += 1
                v3.clear()
        return v2
