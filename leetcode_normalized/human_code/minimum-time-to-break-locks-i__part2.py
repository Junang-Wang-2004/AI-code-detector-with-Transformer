class C1(object):

    def findMinimumTime(self, a1, a2):
        """
        """

        def ceil_divide(a1, a2):
            return (a1 + a2 - 1) // a2

        def popcount(a1):
            return bin(a1).count('1')
        v1 = [float('inf')] * (1 << len(a1))
        v1[0] = 0
        for v2 in range(1, len(v1)):
            v3 = 1 + (popcount(v2) - 1) * a2
            for v4 in range(len(a1)):
                if not v2 & 1 << v4:
                    continue
                v1[v2] = min(v1[v2], v1[v2 ^ 1 << v4] + ceil_divide(a1[v4], v3))
        return v1[-1]
