class C1(object):

    def minCostClimbingStairs(self, a1):
        """
        """
        v1 = [0] * 3
        for v2 in reversed(range(len(a1))):
            v1[v2 % 3] = a1[v2] + min(v1[(v2 + 1) % 3], v1[(v2 + 2) % 3])
        return min(v1[0], v1[1])
