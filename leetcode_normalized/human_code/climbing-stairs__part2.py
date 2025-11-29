class C1(object):
    """
    """

    def climbStairs(self, a1):
        v1, v2 = (0, 1)
        for v3 in range(a1):
            v1, v2 = (v2, v1 + v2)
        return v2
