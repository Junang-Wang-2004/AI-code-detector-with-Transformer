class C1(object):

    def numberOfArrays(self, a1, a2, a3):
        """
        """
        v1 = v2 = v3 = 0
        for v4 in a1:
            v1 += v4
            v2 = min(v2, v1)
            v3 = max(v3, v1)
        return max(a3 - a2 - (v3 - v2) + 1, 0)
