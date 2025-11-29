class C1(object):

    def maxProfit(self, a1):
        """
        """
        if not a1:
            return 0
        v1, v2, v3 = ([0] * 2, [0] * 2, [0] * 2)
        v1[0] = -a1[0]
        for v4 in range(1, len(a1)):
            v1[v4 % 2] = max(v1[(v4 - 1) % 2], v3[(v4 - 1) % 2] - a1[v4])
            v2[v4 % 2] = v1[(v4 - 1) % 2] + a1[v4]
            v3[v4 % 2] = max(v3[(v4 - 1) % 2], v2[(v4 - 1) % 2])
        return max(v3[(len(a1) - 1) % 2], v2[(len(a1) - 1) % 2])
