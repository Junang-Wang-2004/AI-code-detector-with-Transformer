class C1(object):

    def climbStairs(self, a1, a2):
        """
        """
        v1, v2, v3 = (float('inf'), float('inf'), 0)
        for v4 in range(a1):
            v1, v2, v3 = (v2, v3, a2[v4] + min(v1 + 3 ** 2, v2 + 2 ** 2, v3 + 1 ** 2))
        return v3
