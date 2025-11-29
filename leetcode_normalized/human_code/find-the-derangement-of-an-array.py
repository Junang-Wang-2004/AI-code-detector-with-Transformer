class C1(object):

    def findDerangement(self, a1):
        """
        """
        v1 = 1000000007
        v2, v3 = (1, 0)
        for v4 in reversed(range(a1 + 1)):
            v3 = (v3 + v1 + (1 if v4 % 2 == 0 else -1) * v2) % v1
            v2 = v2 * v4 % v1
        return v3
