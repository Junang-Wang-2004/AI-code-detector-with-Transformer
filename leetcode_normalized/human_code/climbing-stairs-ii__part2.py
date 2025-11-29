class C1(object):

    def climbStairs(self, a1, a2):
        """
        """
        v1 = [float('inf')] * (a1 + 1)
        v1[0] = 0
        for v2 in range(a1):
            v1[v2 + 1] = a2[v2] + min((v1[v2 - j] + (j + 1) ** 2 for v3 in range(min(3, v2 + 1))))
        return v1[a1]
